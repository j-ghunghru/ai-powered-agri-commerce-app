from sqlalchemy import Column, Integer, String, Float, ForeignKey
from app.db.database import Base


class Produce(Base):
    __tablename__ = "produces"

    id = Column(Integer, primary_key=True, index=True)
    farmer_id = Column(Integer, ForeignKey("users.id"))
    crop = Column(String)
    quantity = Column(Float)
    grade = Column(String)
    lat = Column(Float)
    lon = Column(Float)
