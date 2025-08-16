from sqlalchemy import Column, Integer, String, Date, Time, Float, ForeignKey, JSON
from sqlalchemy.orm import relationship
from app.database import Base

class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=False)
    vehicle_id = Column(Integer, ForeignKey("vehicles.id"), nullable=False)

    service_type = Column(String, nullable=False)
    service_date = Column(Date, nullable=False)
    service_time = Column(Time, nullable=False)

    spares_list = Column(JSON, nullable=True)  # Optional; can be replaced with junction table later
    labour_charges = Column(Float, nullable=True)
    total_cost = Column(Float, nullable=True)

    issues_name = Column(String, nullable=True)
    issue_reminder_duration = Column(Integer, nullable=True)

    status = Column(String, default="Scheduled")  # e.g., Scheduled, In Progress, Completed
    payment_status = Column(String, default="Pending")  # e.g., Pending, Paid, Failed

    customer = relationship("Customer", back_populates="jobs")
    vehicle = relationship("Vehicle", back_populates="jobs")