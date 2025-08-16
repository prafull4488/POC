from fastapi import FastAPI
from app.database import engine
from app.models import (
    customer as customer_model,
    vehicle as vehicle_model,
    jobs as jobs_model,
    service as service_model,
    labour as labour_model,
    spare as spare_model,
    issue_reminder as reminder_model,
)
from app.routers import (
    customer,
    vehicle,
    jobs,
    service,
    labour,
    spare,
    issue_reminder,
)

app = FastAPI(title="BookAMech API", version="1.0")

# Create tables from models
customer_model.Base.metadata.create_all(bind=engine)
vehicle_model.Base.metadata.create_all(bind=engine)
jobs_model.Base.metadata.create_all(bind=engine)
service_model.Base.metadata.create_all(bind=engine)
labour_model.Base.metadata.create_all(bind=engine)
spare_model.Base.metadata.create_all(bind=engine)
reminder_model.Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(customer.router)
app.include_router(vehicle.router)
app.include_router(jobs.router)
app.include_router(service.router)
app.include_router(labour.router)
app.include_router(spare.router)
app.include_router(issue_reminder.router)