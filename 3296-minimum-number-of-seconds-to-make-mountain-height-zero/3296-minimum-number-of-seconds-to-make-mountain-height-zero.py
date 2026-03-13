class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: list[int]) -> int:
        """
        Find minimum time for workers to reduce mountain to height 0.
        
        For worker i to reduce height by x:
        Time = workerTimes[i] * (1 + 2 + ... + x) = workerTimes[i] * x * (x+1) / 2
        
        Strategy: Binary search on the answer (time)
        For a given time, check if all workers can reduce mountain by at least mountainHeight
        """
        
        def canReduceToZero(time: int) -> bool:
            """Check if workers can reduce mountain by mountainHeight in given time"""
            total_reduction = 0
            
            for worker_time in workerTimes:
                # For this worker, find max height they can reduce in given time
                # using binary search
                max_reduction = binarySearchMaxReduction(worker_time, time)
                total_reduction += max_reduction
                
                # Early termination if we already have enough reduction
                if total_reduction >= mountainHeight:
                    return True
            
            return total_reduction >= mountainHeight
        
        def binarySearchMaxReduction(worker_time: int, available_time: int) -> int:
            """
            Find max height a worker can reduce given available_time
            Using: time_needed = worker_time * x * (x + 1) / 2
            """
            left, right = 0, mountainHeight
            result = 0
            
            while left <= right:
                mid = (left + right) // 2
                # Time needed for this worker to reduce by mid
                time_needed = worker_time * mid * (mid + 1) // 2
                
                if time_needed <= available_time:
                    result = mid
                    left = mid + 1
                else:
                    right = mid - 1
            
            return result
        
        # Binary search on the answer (time)
        # Upper bound: worst case is fastest worker does entire mountain alone
        # For x reductions: time = worker_time * x * (x+1) / 2
        # We need x = mountainHeight, so upper bound = min_worker_time * mountainHeight * (mountainHeight + 1) / 2
        min_worker_time = min(workerTimes)
        upper_bound = min_worker_time * mountainHeight * (mountainHeight + 1) // 2
        
        left, right = 0, upper_bound
        result = right
        
        while left <= right:
            mid = (left + right) // 2
            if canReduceToZero(mid):
                result = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return result


# Test cases
if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    assert sol.minNumberOfSeconds(4, [2, 1, 1]) == 3
    print("Example 1 passed: mountainHeight=4, workerTimes=[2,1,1] → 3")
    
    # Example 2
    assert sol.minNumberOfSeconds(10, [3, 2, 2, 4]) == 12
    print("Example 2 passed: mountainHeight=10, workerTimes=[3,2,2,4] → 12")
    
    # Example 3
    assert sol.minNumberOfSeconds(5, [1]) == 15
    print("Example 3 passed: mountainHeight=5, workerTimes=[1] → 15")
    
    print("\nAll tests passed!")