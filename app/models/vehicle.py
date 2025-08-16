from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Vehicle(Base):
    __tablename__ = "vehicles"

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey("customers.id"))
    registration_number = Column(String, unique=True, nullable=False)
    model = Column(String)
    owner = relationship("Customer", back_populates="vehicles")
    jobs = relationship("Job", back_populates="vehicle")
