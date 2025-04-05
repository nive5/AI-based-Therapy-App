from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
import models, schemas

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/register")
def register_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = models.User(email=user.email, hashed_password=user.password)
    db.add(db_user)
    db.commit()
    return {"message": "User registered successfully"}

@router.get("/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    return user
