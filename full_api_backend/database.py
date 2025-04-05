from sqlalchemy import create_engine
<<<<<<< HEAD
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set. Check your .env file.")
=======
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://username:password@localhost:5432/therapy_db"
>>>>>>> upstream/main

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
<<<<<<< HEAD

'''
from dotenv import load_dotenv
import os
from sqlalchemy import create_engine

# Load environment variables
load_dotenv()

# Get DATABASE_URL from .env
DATABASE_URL = os.getenv("DATABASE_URL")

# Check if DATABASE_URL is loaded correctly


# Create the database engine
engine = create_engine(DATABASE_URL)
'''
=======
>>>>>>> upstream/main
