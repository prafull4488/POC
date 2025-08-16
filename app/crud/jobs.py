from sqlalchemy.orm import Session
from app.models.jobs import Job

def create_job(db: Session, job_data: dict):
    job = Job(**job_data)
    db.add(job)
    db.commit()
    db.refresh(job)
    return job