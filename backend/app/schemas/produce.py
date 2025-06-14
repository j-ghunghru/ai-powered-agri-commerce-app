from pydantic import BaseModel
from typing import List
from typing import Tuple


class ProduceCreate(BaseModel):
    farmer_id: int
    crop: str
    quantity: float
    grade: str
    location: Tuple[float, float]  # (lat, lon)
