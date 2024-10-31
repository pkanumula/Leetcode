from typing import List

class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        # Sort robots and factories by position
        robot.sort()
        factory.sort()
        
        # Number of robots and factories
        r_len = len(robot)
        f_len = len(factory)
        
        # Initialize DP array with infinity
        dp = [float('inf')] * (r_len + 1)
        dp[0] = 0
        
        # Traverse each factory
        for position, limit in factory:
            # Create a temporary DP array to update distances
            new_dp = dp[:]
            # Iterate over each robot and calculate minimal distances within limit
            for i in range(1, r_len + 1):
                total_distance = 0
                # Calculate distances up to the limit
                for k in range(1, min(limit, i) + 1):
                    total_distance += abs(robot[i - k] - position)
                    new_dp[i] = min(new_dp[i], dp[i - k] + total_distance)
            dp = new_dp
        
        # Return the minimum distance to repair all robots
        return dp[r_len]
