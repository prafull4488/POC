from sqlalchemy import Column, Integer, Float, Text, ForeignKey
from app.database import Base

class Labour(Base):
    __tablename__ = "labours"

    id = Column(Integer, primary_key=True)
    job_id = Column(Integer, ForeignKey("jobs.id"))
    description = Column(Text)
    cost = Column(Float)