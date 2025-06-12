from pydantic import BaseModel

class Produce(BaseModel):
    farmer_id: str
    crop: str
    quantity: str
    location_lat: float
    location_lon: float

class MatchInput(BaseModel):
    crop: str
    location_lat: float
    location_lon: float
    max_distance_km: float = 50.0