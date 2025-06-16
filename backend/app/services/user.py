# Description: This code defines the service functions for user management, including creating a user, authenticating a user, and retrieving user information.
# File: backend/app/services/user.py

from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate
from passlib.context import CryptContext
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException
from typing import List, Optional

# This code defines the service functions for user management, including creating a user, authenticating a user, and retrieving user information.
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# This code hashes a password using bcrypt.
def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

# This code verifies a plain password against a hashed password.
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

# This code defines the service function to create a new user in the database.
def create_user(db: Session, user: UserCreate):
    hashed_pw = get_password_hash(user.password)
    db_user = User(
        name=user.name,
        email=user.email,
        password_hash=hashed_pw,
        role=user.role,
        location=user.location,
        phone_number=user.phone_number
    )
    try:
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    except IntegrityError:
        db.rollback()
        return None

# This code defines the service functions for user management, including creating a user, authenticating a user, and retrieving user information.
def authenticate_user(db: Session, phone_number: str, password: str):
    user = db.query(User).filter(User.phone_number == phone_number).first()
    if user and verify_password(password, user.password_hash):
        return {"message": "Login successful", "user_id": user.user_id}
    raise HTTPException(status_code=401, detail="Invalid credentials")

# This code defines the service function to retrieve a user by their phone number.
def get_user_by_id(db: Session, user_id: int) -> Optional[User]:
    return db.query(User).filter(User.user_id == user_id).first()

# This code defines the service function to retrieve all users.
def list_users(db: Session) -> List[User]:
    return db.query(User).all()


