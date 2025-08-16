from sqlalchemy.orm import Session
from app.models.customer import Customer

def create_customer(db: Session, customer_data: dict):
    customer = Customer(**customer_data)
    db.add(customer)
    db.commit()
    db.refresh(customer)
    return customer

def get_customer_by_id(db: Session, customer_id: int):
    return db.query(Customer).filter(Customer.id == customer_id).first()