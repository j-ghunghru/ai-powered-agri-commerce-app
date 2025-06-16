# Description: This module defines the Produce model for the application, which represents agricultural produce listed by farmers.
# File: backend/app/models/produce.py

# import necessary libraries
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from app.db.session import Base

# This code defines the Produce model for the application, which represents agricultural produce listed by farmers.
class Produce(Base):
    __tablename__ = "produces"

    id = Column(Integer, primary_key=True, index=True)
    farmer_id = Column(Integer, ForeignKey("users.user_id"))
    crop = Column(String, nullable=False)
    category = Column(String, nullable=False)
    price_per_unit = Column(Float, nullable=False)
    unit = Column(String, nullable=False)
    quantity = Column(Float, nullable=False)
    grade = Column(String, nullable=False)
    lat = Column(Float, nullable=True)
    lon = Column(Float, nullable=True)
    tags = Column(String)
    listing_date = Column(String)
    description = Column(String)
    image_url = Column(String)
    status = Column(String, default="available")
    location = Column(String)
