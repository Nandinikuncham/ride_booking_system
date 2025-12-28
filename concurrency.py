import threading
from models.user import User
from models.driver import Driver
from models.vehicle import Vehicle
from services.ride_service import RideService

drivers = [
    Driver(101, "Driver A", (1, 1)),
    Driver(102, "Driver B", (2, 2))
]

vehicle = Vehicle("Sedan", 50, 10)

def request_ride(user_id):
    user = User(user_id, f"User{user_id}", (0, 0))
    ride = RideService.request_ride(
        user,
        drivers,
        user.location,
        (10, 10),
        vehicle
    )
    if ride:
        print(f"User {user_id} got Driver {ride.driver.name}")
    else:
        print(f"User {user_id} got no driver")

threads = []
for i in range(5):
    t = threading.Thread(target=request_ride, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
