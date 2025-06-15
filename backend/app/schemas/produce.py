from pydantic import BaseModel, Field
from typing import Optional

# This code defines the Pydantic models for agricultural produce listings, including the base model, creation model, and output model.  
class ProduceBase(BaseModel):
    crop: str
    category: str
    price_per_unit: float
    unit: str
    quantity: float
    grade: str
    lat: Optional[float] = None
    lon: Optional[float] = None
    tags: Optional[str] = None
    listing_date: Optional[str] = None
    description: Optional[str] = None
    image_url: Optional[str] = None
    status: Optional[str] = Field(default="available", pattern="^(available|sold|reserved)$")
    location: Optional[str] = None

class ProduceCreate(ProduceBase):
    farmer_id: int

class ProduceOut(ProduceBase):
    id: int
    farmer_id: int

    model_config = {
        "from_attributes": True
    }
