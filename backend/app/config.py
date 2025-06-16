# Description: Configuration for the database connection using SQLAlchemy.
# File: backend/app/db/config.py

# import necessary libraries
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

SQLALCHEMY_DATABASE_URL = os.getenv("SQLALCHEMY_DATABASE_URL", "sqlite:///./agri_app.db")