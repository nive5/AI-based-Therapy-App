# Full FastAPI Backend for AI Therapy Assistant

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
import models  # Ensure models.py exists
from full_api_backend import schemas

from auth import get_current_user, create_access_token
from chatbot import ai_chat_response
from fastapi.middleware.cors import CORSMiddleware

# Create FastAPI app
app = FastAPI()

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize database
Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/register/")
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(models.User).filter(models.User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    new_user = models.User(email=user.email, hashed_password=user.password)  # Hash password in real scenario
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "User registered successfully"}

@app.post("/login/")
def login(user: schemas.UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if not db_user or db_user.hashed_password != user.password:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token({"sub": user.email})
    return {"access_token": token}

@app.get("/mental_test/")
def mental_test(current_user: schemas.User = Depends(get_current_user)):
    return {"message": "Take the mental health test"}

@app.post("/ai_chat/")
def ai_chat(user_input: schemas.ChatRequest, current_user: schemas.User = Depends(get_current_user)):
    response = ai_chat_response(user_input.message)
    return {"response": response}

@app.get("/tracker/")
def tracker(current_user: schemas.User = Depends(get_current_user)):
    return {"message": "Track your mental health progress"}



