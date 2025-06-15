# This code defines the API endpoints for managing agricultural produce listings by farmers.
# backend/app/routers/produce.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.produce import ProduceCreate, ProduceOut
from app.services import produce as produce_service
from app.services import auth as auth_service
from app.db.session import get_db
from fastapi.security import OAuth2PasswordBearer
from typing import List, Optional

# This code defines the API endpoints for managing agricultural produce listings by farmers.
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/login")
router = APIRouter()

# This code defines the API endpoint to create a new produce listing.
@router.post("/", response_model=ProduceOut)
def create_produce(
    produce: ProduceCreate,
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):
    payload = auth_service.decode_access_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid token")

    if payload.get("role") != "farmer":
        raise HTTPException(status_code=403, detail="Only farmers can publish produce")

    return produce_service.create_produce(db, produce)

# This code defines the API endpoint to list all produce listings.
@router.get("/", response_model=List[ProduceOut])
def list_produce(db: Session = Depends(get_db)):
    return produce_service.list_produce(db)

# This code defines the API endpoint to get a specific produce listing by its ID.
@router.get("/{produce_id}", response_model=Optional[ProduceOut])
def get_produce(produce_id: int, db: Session = Depends(get_db)):
    produce = produce_service.get_produce_by_id(db, produce_id)
    if not produce:
        raise HTTPException(status_code=404, detail="Produce not found")
    return produce