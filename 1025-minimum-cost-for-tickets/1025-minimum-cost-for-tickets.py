from typing import List

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # Initialize a set for quick lookup of travel days
        travel_days = set(days)
        # Initialize a dp array where dp[i] represents the minimum cost to cover up to day i
        dp = [0] * (days[-1] + 1)

        for day in range(1, days[-1] + 1):
            if day not in travel_days:
                # If no travel on this day, cost remains the same as the previous day
                dp[day] = dp[day - 1]
            else:
                # Calculate the minimum cost among 1-day, 7-day, and 30-day passes
                dp[day] = min(
                    dp[max(0, day - 1)] + costs[0],  # 1-day pass
                    dp[max(0, day - 7)] + costs[1],  # 7-day pass
                    dp[max(0, day - 30)] + costs[2]  # 30-day pass
                )

        return dp[days[-1]]
