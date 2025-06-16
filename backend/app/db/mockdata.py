# Description: Mock data seeding for the application
# File: backend/app/db/mockdata.py

# import necessary libraries
import random
from faker import Faker
from datetime import datetime
from sqlalchemy.orm import Session

# Ensure the Faker library is installed: pip install faker
fake = Faker()

# Function to seed mock data into the database
def seed_mock_data(db: Session):
    # ✅ Import models inside the function to avoid circular import issues
    from app.models.user import User
    from app.models.produce import Produce

    if db.query(User).first():
        return

    farmers = [
        User(
            name=fake.name(),
            email=fake.email(),
            password_hash="hashed_pw",
            role="farmer",
            location=fake.city(),
            phone_number=fake.phone_number()
        )
        for _ in range(10)
    ]

    buyers = [
        User(
            name=fake.name(),
            email=fake.email(),
            password_hash="hashed_pw",
            role="buyer",
            location=fake.city(),
            phone_number=fake.phone_number()
        )
        for _ in range(10)
    ]

    db.add_all(farmers + buyers)
    db.commit()

    farmer_ids = [f.user_id for f in db.query(User).filter(User.role == "farmer").all()]

    categories = ["fruit", "vegetable", "grain"]
    grades = ["organic", "conventional"]
    units = ["kg", "ton", "bunch"]

    produces = [
        Produce(
            farmer_id=random.choice(farmer_ids),
            crop=fake.word(),
            category=random.choice(categories),
            price_per_unit=round(random.uniform(10, 100), 2),
            unit=random.choice(units),
            quantity=round(random.uniform(5, 50), 2),
            grade=random.choice(grades),
            lat=round(fake.latitude(), 6),
            lon=round(fake.longitude(), 6),
            tags="fresh,local",
            listing_date=datetime.now().date().isoformat(),
            description=fake.sentence(),
            image_url=fake.image_url(),
            status="available",
            location=fake.city()
        )
        for _ in range(20)
    ]

    db.add_all(produces)
    db.commit()