from sqlalchemy import Column, Integer, String, Float
from .database import Base

class Produce(Base):
    __tablename__ = "produce"
    id = Column(Integer, primary_key=True, index=True)
    farmer_id = Column(String)
    crop = Column(String)
    quantity = Column(String)
    location_lat = Column(Float)
    location_lon = Column(Float)