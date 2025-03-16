from typing import List

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def canRepairInTime(mid: int) -> bool:
            total_cars = 0
            for rank in ranks:
                total_cars += int((mid // rank) ** 0.5)  # Maximum cars mechanic can repair within 'mid' time
                if total_cars >= cars:
                    return True
            return total_cars >= cars
        
        left, right = 1, min(ranks) * (cars ** 2)  # Upper bound using the slowest mechanic repairing all cars
        while left < right:
            mid = (left + right) // 2
            if canRepairInTime(mid):
                right = mid  # Try for a smaller time
            else:
                left = mid + 1  # Increase the time
        
        return left
