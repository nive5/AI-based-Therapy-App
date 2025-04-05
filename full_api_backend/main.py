from fastapi import FastAPI
from routers import auth, chatbot

app = FastAPI()

# Include routers
app.include_router(auth.router, prefix="/auth")
app.include_router(chatbot.router)
