from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.jobs import JobCreate, JobOut
from app.crud.jobs import create_job  # assuming you have this

router = APIRouter(prefix="/jobs", tags=["Jobs"])

@router.post("/", response_model=JobOut)
def create_job_endpoint(job: JobCreate, db: Session = Depends(get_db)):
    return create_job(db, job.dict())