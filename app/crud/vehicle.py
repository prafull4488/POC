from sqlalchemy.orm import Session
from app.models.vehicle import Vehicle

def create_vehicle(db: Session, vehicle_data: dict):
    vehicle = Vehicle(**vehicle_data)
    db.add(vehicle)
    db.commit()
    db.refresh(vehicle)
    return vehicle

def get_vehicles_by_customer(db: Session, customer_id: int):
    return db.query(Vehicle).filter(Vehicle.customer_id == customer_id).all()