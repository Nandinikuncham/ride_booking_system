from utils.distance import calculate_distance

class FareService:
    @staticmethod
    def calculate_fare(source, destination, vehicle, surge_multiplier=1.0):
        distance = calculate_distance(source, destination)
        base_fare = vehicle.base_fare + (distance * vehicle.per_km_rate)
        return round(base_fare * surge_multiplier, 2)
