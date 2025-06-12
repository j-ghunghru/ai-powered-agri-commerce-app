from sqlalchemy import Column, Integer, String, Float, ForeignKey
from database import Base

class Produce(Base):
    __tablename__ = "produces"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    description = Column(String, nullable=True)
    quantity_kg = Column(Float, nullable=False)
    price_per_kg = Column(Float, nullable=False)
    farmer_id = Column(Integer, ForeignKey("users.id"), nullable=False)
