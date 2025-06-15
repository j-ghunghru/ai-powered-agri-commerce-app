from sqlalchemy import Column, Integer, Text, CheckConstraint, DateTime, func
from app.db.session import Base

# This code defines the User model for the application, which represents users in the system.
class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(Text, nullable=False)
    email = Column(Text, unique=True, nullable=True)
    password_hash = Column(Text, nullable=False)
    role = Column(Text, nullable=False)
    location = Column(Text)
    phone_number = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.current_timestamp())

    __table_args__ = (
        CheckConstraint("role IN ('farmer', 'buyer')", name="check_role_valid"),
    )
