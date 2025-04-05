from fastapi import FastAPI
from routers import user, auth, chatbot

app = FastAPI()

app.include_router(user.router)
app.include_router(auth.router)
app.include_router(chatbot.router)

@app.get("/")
def home():
    return {"message": "AI Therapy API is running"}
