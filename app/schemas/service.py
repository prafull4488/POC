from pydantic import BaseModel
from typing import Optional

class ServiceCreate(BaseModel):
    name: str
    description: Optional[str] = None
    base_price: Optional[float] = None
    estimated_duration: Optional[int] = None
    reminder_duration: Optional[int] = None

class ServiceOut(ServiceCreate):
    id: int

    class Config:
        from_attributes = True  # Pydantic v2 compatible