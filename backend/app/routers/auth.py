from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserLogin
from app.services.auth import register_user, authenticate_user, create_token
from app.db.session import get_db

router = APIRouter()

@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    return register_user(user, db)

@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    return authenticate_user(user, db)