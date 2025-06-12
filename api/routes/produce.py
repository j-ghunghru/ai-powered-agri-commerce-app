from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
from models.schemas import ProduceCreate, ProduceOut
from sqlalchemy_models.produce import Produce
from sqlalchemy_models.user import User
from database import get_db
from auth import decode_access_token

router = APIRouter(prefix="/produce", tags=["Produce"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/login")

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> User:
    payload = decode_access_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    user = db.query(User).filter(User.email == payload.get("sub")).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("/register", response_model=ProduceOut)
def register_produce(produce: ProduceCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    if current_user.role != "farmer":
        raise HTTPException(status_code=403, detail="Only farmers can register produce.")
    db_produce = Produce(**produce.dict(), farmer_id=current_user.id)
    db.add(db_produce)
    db.commit()
    db.refresh(db_produce)
    return db_produce

@router.get("/list", response_model=list[ProduceOut])
def list_produce(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(Produce).offset(skip).limit(limit).all()
