'''
from fastapi import APIRouter
from chatbot.custom_chatbot import generate_response

router = APIRouter(prefix="/chatbot", tags=["Chatbot"])

@router.post("/message")
def chat_with_ai(user_input: str):
    response = generate_response(user_input)
    return {"response": response}
'''

import openai
import os
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

# Load API key from environment variable (Set it before running)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

class ChatRequest(BaseModel):
    message: str

@router.post("/chat")
async def ai_chat(request: ChatRequest):
    if not OPENAI_API_KEY:
        raise HTTPException(status_code=500, detail="OpenAI API Key is missing")
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": request.message}]
        )
        return {"response": response["choices"][0]["message"]["content"]}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
