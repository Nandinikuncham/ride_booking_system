class Driver:
    def __init__(self, driver_id, name, location):
        self.driver_id = driver_id
        self.name = name
        self.location = location
        self.available = True
        self.rating = 5.0
        self.total_rides = 0

    def update_rating(self, new_rating):
        self.rating = (
            (self.rating * self.total_rides + new_rating)
            / (self.total_rides + 1)
        )
        self.total_rides += 1
