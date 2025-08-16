from app.database import engine
from app.models import Base, Customer, Job  # Import the shared Base
print("Tables registered:", Base.metadata.tables.keys())  # Debug line
Base.metadata.create_all(bind=engine)
print("✅ Database initialized.")