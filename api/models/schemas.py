from pydantic import BaseModel, EmailStr
from typing import Optional, Literal

class UserBase(BaseModel):
    name: str
    email: EmailStr
    phone: str
    role: Literal["farmer", "buyer"]

class UserCreate(UserBase):
    password: str

class UserOut(UserBase):
    id: int

    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class ProduceBase(BaseModel):
    name: str
    description: Optional[str] = None
    quantity_kg: float
    price_per_kg: float

class ProduceCreate(ProduceBase):
    pass

class ProduceOut(ProduceBase):
    id: int
    farmer_id: int

    class Config:
        orm_mode = True
