from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.produce import ProduceCreate
from app.services.produce import create_produce
from app.db.session import get_db
from app.models.produce import Produce  # ✅ Needed for the GET endpoint

router = APIRouter(prefix="/produce", tags=["Produce"])

# POST /produce - Publish new produce (only by sellers)
@router.post("/")
def publish_produce(produce: ProduceCreate, db: Session = Depends(get_db)):
    return create_produce(produce, db)

# GET /produce - List all produce
@router.get("/")
def list_all_produce(db: Session = Depends(get_db)):
    return db.query(Produce).all()
