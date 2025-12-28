class Ride:
    def __init__(self, ride_id, user, driver, source, destination, fare, eta):
        self.ride_id = ride_id
        self.user = user
        self.driver = driver
        self.source = source
        self.destination = destination
        self.fare = fare
        self.eta = eta
        self.status = "ASSIGNED"

    def start_ride(self):
        self.status = "IN_PROGRESS"

    def complete_ride(self, rating):
        self.status = "COMPLETED"
        self.driver.available = True
        self.driver.update_rating(rating)

    def cancel_ride(self):
        self.status = "CANCELLED"
        self.driver.available = True
