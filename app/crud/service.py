from sqlalchemy.orm import Session
from app.models.service import Service

def create_service(db: Session, service_data: dict):
    service = Service(**service_data)
    db.add(service)
    db.commit()
    db.refresh(service)
    return service

def list_services(db: Session):
    return db.query(Service).all()