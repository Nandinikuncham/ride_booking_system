import heapq
from utils.distance import calculate_distance
from utils.lock import driver_assignment_lock

class MatchingService:
    @staticmethod
    def find_nearest_driver(user_location, drivers):
        with driver_assignment_lock:
            heap = []

            for driver in drivers:
                if driver.available:
                    distance = calculate_distance(user_location, driver.location)
                    heapq.heappush(
                        heap,
                        (distance, driver.driver_id, driver)
                    )

            if not heap:
                return None

            selected_driver = heapq.heappop(heap)[2]
            selected_driver.available = False  # lock-protected

            return selected_driver
