from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from db.database import SessionLocal, engine
from db.models import Base, User, Driver, Ride
from pydantic import BaseModel

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Ride Booking System")

# Enable full CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all origins
    allow_credentials=True,
    allow_methods=["*"],   # allow GET, POST, etc.
    allow_headers=["*"],
)

# ----------------- Pydantic Schemas -----------------
class RideRequest(BaseModel):
    user_id: int
    destination_x: int
    destination_y: int
    vehicle_type: str

class RideComplete(BaseModel):
    ride_id: int
    rating: float

# ----------------- Helpers -----------------
def calculate_fare(x, y, vehicle_type):
    distance = (x**2 + y**2)**0.5
    base_fare = {"Mini":50, "Sedan":100, "SUV":150}
    return round(base_fare.get(vehicle_type, 100) + distance*10, 2)

def assign_driver(db: Session):
    driver = db.query(Driver).filter(Driver.available==True).first()
    if not driver:
        driver = db.query(Driver).first()
    driver.available = False
    db.commit()
    return driver

# ----------------- API Endpoints -----------------
@app.post("/ride/request")
def request_ride(req: RideRequest):
    db = SessionLocal()
    user = db.query(User).filter(User.id==req.user_id).first()
    if not user:
        db.close()
        return {"error":"User not found"}

    driver = assign_driver(db)
    fare = calculate_fare(req.destination_x, req.destination_y, req.vehicle_type)

    ride = Ride(
        user_id=user.id,
        driver_id=driver.id,
        vehicle_type=req.vehicle_type,
        destination_x=req.destination_x,
        destination_y=req.destination_y,
        fare=fare,
        status="ASSIGNED"
    )
    db.add(ride)
    db.commit()
    db.refresh(ride)
    db.close()
    return {
        "ride_id": ride.id,
        "driver": driver.name,
        "vehicle": ride.vehicle_type,
        "fare": ride.fare,
        "status": ride.status
    }

@app.post("/ride/complete")
def complete_ride(rc: RideComplete):
    db = SessionLocal()
    ride = db.query(Ride).filter(Ride.id==rc.ride_id).first()
    if not ride:
        db.close()
        return {"error":"Ride not found"}

    driver = db.query(Driver).filter(Driver.id==ride.driver_id).first()
    ride.status = "COMPLETED"
    driver.rating = round((driver.rating + rc.rating)/2, 2)
    driver.available = True

    db.commit()
    db.close()
    return {"status": ride.status, "driver_rating": driver.rating}

@app.get("/ride/history/{user_id}")
def ride_history(user_id: int):
    db = SessionLocal()
    rides_db = db.query(Ride).filter(Ride.user_id==user_id).all()
    rides = []
    for r in rides_db:
        driver = db.query(Driver).filter(Driver.id==r.driver_id).first()
        rides.append({
            "ride_id": r.id,
            "driver": driver.name if driver else "Unknown",
            "fare": r.fare,
            "status": r.status
        })
    db.close()
    return {"rides": rides}
