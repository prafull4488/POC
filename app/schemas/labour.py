from pydantic import BaseModel

class LabourCreate(BaseModel):
    job_id: int
    description: str
    cost: float

class LabourOut(LabourCreate):
    id: int

    class Config:
        from_attributes = True  # Pydantic v2 compatible