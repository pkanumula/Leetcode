from collections import defaultdict

class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        # Dictionary to store the number of ways to reach each sum
        dp = defaultdict(int)
        dp[0] = 1  # Initial state: one way to reach sum 0

        for num in nums:
            next_dp = defaultdict(int)
            for s, count in dp.items():
                next_dp[s + num] += count
                next_dp[s - num] += count
            dp = next_dp

        return dp[target]
