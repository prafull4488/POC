from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.service import ServiceCreate, ServiceOut
from app.crud.service import create_service, list_services
from typing import List

router = APIRouter(prefix="/services", tags=["Services"])

@router.post("/", response_model=ServiceOut)
def create_service_endpoint(service: ServiceCreate, db: Session = Depends(get_db)):
    return create_service(db, service.dict())

@router.get("/", response_model=List[ServiceOut])
def get_all_services(db: Session = Depends(get_db)):
    return list_services(db)