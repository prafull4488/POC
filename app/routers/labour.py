from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.labour import LabourCreate, LabourOut
from app.crud.labour import add_labour_entry, get_labour_by_job
from typing import List

router = APIRouter(prefix="/labour", tags=["Labour"])

@router.post("/", response_model=LabourOut)
def add_labour(labour: LabourCreate, db: Session = Depends(get_db)):
    return add_labour_entry(db, labour.dict())

@router.get("/by_job/{job_id}", response_model=List[LabourOut])
def get_labour(job_id: int, db: Session = Depends(get_db)):
    return get_labour_by_job(db, job_id)