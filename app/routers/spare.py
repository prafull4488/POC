from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.spare import SpareCreate, SpareOut
from app.crud.spare import add_spare_part, get_spares_by_job
from typing import List

router = APIRouter(prefix="/spares", tags=["Spares"])

@router.post("/", response_model=SpareOut)
def add_spare(spare: SpareCreate, db: Session = Depends(get_db)):
    return add_spare_part(db, spare.dict())

@router.get("/by_job/{job_id}", response_model=List[SpareOut])
def get_spares(job_id: int, db: Session = Depends(get_db)):
    return get_spares_by_job(db, job_id)