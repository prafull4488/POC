from sqlalchemy import Column, Integer, String, Float, ForeignKey
from app.database import Base

class Spare(Base):
    __tablename__ = "spares"

    id = Column(Integer, primary_key=True)
    job_id = Column(Integer, ForeignKey("jobs.id"))
    part_name = Column(String)
    cost = Column(Float)
    quantity = Column(Integer)