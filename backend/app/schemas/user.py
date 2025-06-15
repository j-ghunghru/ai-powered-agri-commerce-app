from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime

class UserBase(BaseModel):
    name: str
    email: Optional[EmailStr] = None
    role: str = Field(..., pattern="^(farmer|buyer)$")
    location: Optional[str] = None
    phone_number: str

class UserCreate(UserBase):
    password: str

class UserOut(UserBase):
    user_id: int
    created_at: datetime

    model_config = {
        "from_attributes": True
    }

class UserLogin(BaseModel):
    phone_number: str
    password: str
