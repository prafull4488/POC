from sqlalchemy.orm import Session
from app.models.labour import Labour

def add_labour_entry(db: Session, labour_data: dict):
    labour = Labour(**labour_data)
    db.add(labour)
    db.commit()
    db.refresh(labour)
    return labour

def get_labour_by_job(db: Session, job_id: int):
    return db.query(Labour).filter(Labour.job_id == job_id).all()