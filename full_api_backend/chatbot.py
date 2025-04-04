def ai_chat_response(message: str) -> str:
    """
    Simulates an AI chatbot response.
    Replace this with an actual AI model in the future.
    """
    responses = {
        "hello": "Hello! How can I help you today?",
        "how are you": "I'm just a chatbot, but I'm here to assist you!",
        "bye": "Goodbye! Take care!",
    }
    
    # Convert message to lowercase and match response
    return responses.get(message.lower(), "I'm here to listen. Tell me more.")
