from sqlalchemy import Column, Integer, String
from database import Base
from full_api_backend import models, schemas, auth, chatbot


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)