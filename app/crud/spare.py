from sqlalchemy.orm import Session
from app.models.spare import Spare

def add_spare_part(db: Session, spare_data: dict):
    spare = Spare(**spare_data)
    db.add(spare)
    db.commit()
    db.refresh(spare)
    return spare

def get_spares_by_job(db: Session, job_id: int):
    return db.query(Spare).filter(Spare.job_id == job_id).all()