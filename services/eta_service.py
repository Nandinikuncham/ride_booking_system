from utils.distance import calculate_distance

class ETAService:
    @staticmethod
    def calculate_eta(source, destination, speed=40):
        distance = calculate_distance(source, destination)
        return distance / speed  # hours
