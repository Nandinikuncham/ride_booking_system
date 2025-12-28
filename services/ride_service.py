from models.Ride import Ride
from services.matching_service import MatchingService
from services.fare_service import FareService
from services.eta_service import ETAService
from services.surge_service import SurgeService

class RideService:
    ride_counter = 1
    ride_history = []

    @staticmethod
    def request_ride(user, drivers, source, destination, vehicle):
        driver = MatchingService.find_nearest_driver(source, drivers)
        if not driver:
            return None

        active_rides = len([r for r in RideService.ride_history if r.status != "COMPLETED"])
        available_drivers = len([d for d in drivers if d.available])

        surge = SurgeService.calculate_surge(active_rides, available_drivers)

        fare = FareService.calculate_fare(
            source, destination, vehicle, surge
        )

        eta = ETAService.calculate_eta(source, destination)

        driver.available = False

        ride = Ride(
            RideService.ride_counter,
            user,
            driver,
            source,
            destination,
            fare,
            eta
        )

        RideService.ride_counter += 1
        RideService.ride_history.append(ride)
        return ride

    @staticmethod
    def start_ride(ride):
        ride.start_ride()

    @staticmethod
    def complete_ride(ride, rating):
        ride.complete_ride(rating)
