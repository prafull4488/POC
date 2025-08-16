from sqlalchemy import Column, Integer, String, Float, Text
from app.database import Base

class Service(Base):
    __tablename__ = "services"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(Text)
    base_price = Column(Float)
    estimated_duration = Column(Integer)  # in minutes or hours
    reminder_duration = Column(Integer)  # in days or weeks