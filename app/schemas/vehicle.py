from pydantic import BaseModel
from typing import Optional

class VehicleCreate(BaseModel):
    customer_id: int
    registration_number: str
    model: Optional[str] = None

class VehicleOut(VehicleCreate):
    id: int

    class Config:
        from_attributes = True  # Pydantic v2 compatible