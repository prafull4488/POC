from pydantic import BaseModel
from typing import Optional
from datetime import date, time

class JobCreate(BaseModel):
    customer_id: int
    vehicle_id: int
    service_type: str
    service_date: date
    service_time: time
    spares_list: Optional[dict] = None
    labour_charges: Optional[float] = None
    total_cost: Optional[float] = None
    issues_name: Optional[str] = None
    issue_reminder_duration: Optional[int] = None
    status: Optional[str] = "Scheduled"
    payment_status: Optional[str] = "Pending"

class JobOut(JobCreate):
    id: int

    class Config:
        from_attributes = True  # Pydantic v2 compatible