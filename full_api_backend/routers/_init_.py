from fastapi import APIRouter

# Import all router modules
from routers import chatbot, auth, users

# Create a main router
router = APIRouter()

# Include different route modules
router.include_router(chatbot.router)
router.include_router(auth.router)
router.include_router(users.router)
