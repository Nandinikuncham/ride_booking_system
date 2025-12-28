class SurgeService:
    @staticmethod
    def calculate_surge(active_rides, available_drivers):
        if available_drivers == 0:
            return 3.0

        surge = active_rides / available_drivers

        if surge < 1.2:
            return 1.0

        return min(round(surge, 2), 3.0)
