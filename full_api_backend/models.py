from sqlalchemy import Column, Integer, String
from database import Base
<<<<<<< HEAD
from full_api_backend import models, schemas, auth, chatbot

=======
>>>>>>> upstream/main

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
<<<<<<< HEAD
    hashed_password = Column(String)
=======
    hashed_password = Column(String)
>>>>>>> upstream/main
