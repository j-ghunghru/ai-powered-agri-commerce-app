from fastapi import HTTPException
from app.models.user import User
from app.schemas.user import UserCreate, UserLogin
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
SECRET_KEY = "supersecretkey"
ALGORITHM = "HS256"

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def create_token(username: str) -> str:
    expire = datetime.utcnow() + timedelta(minutes=30)
    to_encode = {"sub": username, "exp": expire}
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def register_user(user: UserCreate, db: Session):
    if db.query(User).filter(User.username == user.username).first():
        raise HTTPException(status_code=400, detail="Username already exists")
    db_user = User(
        username=user.username,
        hashed_password=hash_password(user.password),
        role=user.role
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {"message": "User registered"}

def authenticate_user(user: UserLogin, db: Session):
    db_user = db.query(User).filter(User.username == user.username).first()
    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_token(db_user.username)
    return {"access_token": token, "token_type": "bearer"}