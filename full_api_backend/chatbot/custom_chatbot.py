from transformers import pipeline
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()
chatbot = pipeline("text-generation", model="facebook/blenderbot-400M-distill")

class ChatRequest(BaseModel):
    message: str

@router.post("/chat")
async def chat_with_nlp(request: ChatRequest):
    response = chatbot(request.message, max_length=50)
    return {"reply": response[0]["generated_text"]}
