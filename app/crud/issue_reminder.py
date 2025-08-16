from sqlalchemy.orm import Session
from app.models.issue_reminder import IssueReminder

def schedule_reminder(db: Session, reminder_data: dict):
    reminder = IssueReminder(**reminder_data)
    db.add(reminder)
    db.commit()
    db.refresh(reminder)
    return reminder

def get_pending_reminders(db: Session):
    return db.query(IssueReminder).filter(IssueReminder.sent == False).all()