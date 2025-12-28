from db.database import engine, SessionLocal
from db.models import Base, User, Driver

# Create tables
Base.metadata.create_all(bind=engine)

db = SessionLocal()

# Add sample users
if db.query(User).count() == 0:
    db.add_all([User(name="Nandu"), User(name="Alice")])
    db.commit()

# Add sample drivers
if db.query(Driver).count() == 0:
    db.add_all([
        Driver(name="Driver A"),
        Driver(name="Driver B"),
        Driver(name="Driver C")
    ])
    db.commit()

db.close()
print("Database initialized with sample users and drivers")
