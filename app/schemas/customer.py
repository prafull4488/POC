from pydantic import BaseModel
from typing import Optional

class CustomerCreate(BaseModel):
    name: str
    phone: str
    email: Optional[str] = None

class CustomerOut(CustomerCreate):
    id: int

    class Config:
        from_attributes = True  # Pydantic v2 compatible