from pydantic import BaseModel, EmailStr

# User Registration Schema
class UserCreate(BaseModel):
    email: EmailStr
    password: str

# User Login Schema
class UserLogin(BaseModel):
    email: EmailStr
    password: str

# User Response Schema (for protected routes)
class User(BaseModel):
    email: EmailStr

    class Config:
        from_attributes = True  # For SQLAlchemy ORM compatibility

# Chat Request Schema
class ChatRequest(BaseModel):
    message: str
