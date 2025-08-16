from app.database import SessionLocal
from app.models import Customer, Job

# Create a new DB session
session = SessionLocal()

try:
    # Create a sample customer
    customer = Customer(
        name="Sindhu",
        email="sindhu@example.com",
        phone="9876543210"
    )
    session.add(customer)
    session.flush()  # Get customer.id before committing

    # Create a sample job linked to the customer
    job = Job(
        customer_id=customer.id,
        vehicle="Honda City",
        service_type="Oil Change",
        status="Scheduled"
    )
    session.add(job)

    # Commit both inserts
    session.commit()
    print("✅ Sample customer and job inserted.")

except Exception as e:
    session.rollback()
    print("❌ Insert failed:", e)

finally:
    session.close()