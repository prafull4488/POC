from pydantic import BaseModel

class SpareCreate(BaseModel):
    job_id: int
    part_name: str
    cost: float
    quantity: int

class SpareOut(SpareCreate):
    id: int

    class Config:
        from_attributes = True  # Pydantic v2 compatible