from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.vehicle import VehicleCreate, VehicleOut
from app.crud.vehicle import create_vehicle, get_vehicles_by_customer
from typing import List

router = APIRouter(prefix="/vehicles", tags=["Vehicles"])

@router.post("/", response_model=VehicleOut)
def create_vehicle_endpoint(vehicle: VehicleCreate, db: Session = Depends(get_db)):
    return create_vehicle(db, vehicle.dict())

@router.get("/by_customer/{customer_id}", response_model=List[VehicleOut])
def list_vehicles(customer_id: int, db: Session = Depends(get_db)):
    return get_vehicles_by_customer(db, customer_id)