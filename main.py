from models.User import User
from models.Driver import Driver
from models.Vehicle import Vehicle
from services.ride_service import RideService

def main():
    user = User(1, "Nandu", (2, 3))

    drivers = [
        Driver(101, "Driver A", (1, 1)),
        Driver(102, "Driver B", (5, 5)),
        Driver(103, "Driver C", (2, 4))
    ]

    sedan = Vehicle("Sedan", 50, 10)

    ride = RideService.request_ride(
        user=user,
        drivers=drivers,
        source=user.location,
        destination=(10, 10),
        vehicle=sedan
    )

    print(f"Ride ID: {ride.ride_id}")
    print(f"Driver: {ride.driver.name}")
    print(f"Vehicle: {sedan.vehicle_type}")
    print(f"Fare (with surge): ₹{ride.fare}")
    print(f"Driver Rating (before): {ride.driver.rating}")

    RideService.start_ride(ride)
    RideService.complete_ride(ride, rating=4.5)

    print(f"Ride Status: {ride.status}")
    print(f"Driver Rating (after): {ride.driver.rating:.2f}")

if __name__ == "__main__":
    main()
