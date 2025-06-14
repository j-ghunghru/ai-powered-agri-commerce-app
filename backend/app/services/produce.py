from app.models.produce import Produce
from app.schemas.produce import ProduceCreate
from app.models.user import User  # Fixed relative import
from sqlalchemy.orm import Session
from fastapi import HTTPException

def create_produce(produce: ProduceCreate, db: Session):
    # Check if farmer exists and has 'seller' role
    farmer = db.query(User).filter(User.id == produce.farmer_id).first()
    if not farmer or farmer.role.lower() != "seller":
        raise HTTPException(status_code=403, detail="Only users with 'seller' role can publish produce")

    # Create and save new produce
    new_produce = Produce(
        farmer_id=produce.farmer_id,
        crop=produce.crop,
        quantity=produce.quantity,
        grade=produce.grade,
        lat=produce.location[0],
        lon=produce.location[1]
    )
    db.add(new_produce)
    db.commit()
    db.refresh(new_produce)

    return {
        "message": "Produce published successfully",
        "produce_id": new_produce.id
    }
