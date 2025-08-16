from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.issue_reminder import IssueReminderCreate, IssueReminderOut
from app.crud.issue_reminder import schedule_reminder, get_pending_reminders
from typing import List

router = APIRouter(prefix="/reminders", tags=["Issue Reminders"])

@router.post("/", response_model=IssueReminderOut)
def create_reminder(reminder: IssueReminderCreate, db: Session = Depends(get_db)):
    return schedule_reminder(db, reminder.dict())

@router.get("/pending", response_model=List[IssueReminderOut])
def list_pending_reminders(db: Session = Depends(get_db)):
    return get_pending_reminders(db)