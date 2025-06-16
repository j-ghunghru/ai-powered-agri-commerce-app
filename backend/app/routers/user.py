# Description: This code defines the API endpoints for user management, including registration, login, and profile retrieval.
# File: backend/app/routers/user.py

# import necessary libraries
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from app.schemas.user import UserCreate, UserLogin, UserOut
from app.services import user as user_service
from app.services import auth as auth_service
from app.db.session import get_db
from jose import JWTError
from typing import Annotated
from typing import List

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/login")

# This code defines the API endpoints for user registration, login, and profile management.
@router.post("/register", response_model=UserOut)
def register(user: UserCreate, db: Session = Depends(get_db)):
    db_user = user_service.create_user(db, user)
    if not db_user:
        raise HTTPException(status_code=400, detail="User with this phone or email already exists")
    return db_user

# This code defines the API endpoint for user login.
@router.post("/login")
def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: Session = Depends(get_db)):
    user = user_service.get_user_by_phone(db, form_data.username)
    if not user or not auth_service.verify_password(form_data.password, user.password_hash):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    token_data = {"sub": str(user.user_id), "role": user.role}
    token = auth_service.create_access_token(token_data)
    return {"access_token": token, "token_type": "bearer"}

# This code defines the API endpoint to get the current user's profile.
@router.get("/me", response_model=UserOut)
def read_users_me(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    payload = auth_service.decode_access_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid token")
    user = user_service.get_user_by_id(db, int(payload.get("sub")))
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# This code defines the API endpoints for user management, including getting a user by ID and listing all users.
@router.get("/{user_id}", response_model=UserOut)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = user_service.get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# This code defines the API endpoint to list all users.
@router.get("/", response_model=List[UserOut])
def list_all_users(db: Session = Depends(get_db)):
    return user_service.list_users(db)