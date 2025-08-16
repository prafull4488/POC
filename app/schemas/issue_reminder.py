from pydantic import BaseModel
from datetime import datetime

class IssueReminderCreate(BaseModel):
    customer_id: int
    message: str
    scheduled_date: datetime

class IssueReminderOut(IssueReminderCreate):
    id: int
    sent: bool

    class Config:
        from_attributes = True  # Pydantic v2 compatible