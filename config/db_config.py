import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

# Load .env file automatically
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set. Please check your .env file.")

engine = create_engine(DATABASE_URL)
