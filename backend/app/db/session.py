# Description: This module sets up the database session and initializes the database.
# File: backend/app/db/session.py

# Import necessary libraries
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.db.mockdata import seed_mock_data
from app.config import SQLALCHEMY_DATABASE_URL

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Initialize and seed database
def init_db():
    from app.models import user, produce
    Base.metadata.create_all(bind=engine)

    # Seed mock data only if not present
    db = SessionLocal()
    try:
        seed_mock_data(db)
    finally:
        db.close()

# Function to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()