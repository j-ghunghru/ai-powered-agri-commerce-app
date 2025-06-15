# This code defines the service functions for managing agricultural produce listings, including creating, listing, and retrieving produce by ID.
# backend/app/services/produce.py

from sqlalchemy.orm import Session
from app.models.produce import Produce
from app.schemas.produce import ProduceCreate
from typing import List, Optional

# This code defines the service functions for managing agricultural produce listings, including creating, listing, and retrieving produce by ID.
def create_produce(db: Session, produce: ProduceCreate) -> Produce:
    db_produce = Produce(**produce.model_dump())
    db.add(db_produce)
    db.commit()
    db.refresh(db_produce)
    return db_produce

# This code defines the service functions for managing agricultural produce listings, including creating, listing, and retrieving produce by ID.
def list_produce(db: Session) -> List[Produce]:
    return db.query(Produce).all()

# This code defines the service function to retrieve a specific produce listing by its ID.
def get_produce_by_id(db: Session, produce_id: int) -> Optional[Produce]:
    return db.query(Produce).filter(Produce.id == produce_id).first()
