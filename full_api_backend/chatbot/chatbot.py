from fastapi import APIRouter
from chatbot.custom_chatbot import generate_response

router = APIRouter(prefix="/chatbot", tags=["Chatbot"])

@router.post("/message")
def chat_with_ai(user_input: str):
    response = generate_response(user_input)
    return {"response": response}
