from sqlalchemy import Column, Integer, Text, DateTime, Boolean, ForeignKey
from app.database import Base

class IssueReminder(Base):
    __tablename__ = "issue_reminders"

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey("customers.id"))
    message = Column(Text)
    scheduled_date = Column(DateTime)
    sent = Column(Boolean, default=False)