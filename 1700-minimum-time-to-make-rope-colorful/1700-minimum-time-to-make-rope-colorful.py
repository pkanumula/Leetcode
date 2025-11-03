from typing import List

class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        total = 0
        # max_time_in_run stores the largest neededTime in the current run of same-colored balloons
        max_time_in_run = neededTime[0]

        for i in range(1, len(colors)):
            if colors[i] == colors[i - 1]:
                # Same color as previous: remove the cheaper one
                total += min(max_time_in_run, neededTime[i])
                # Keep the more expensive one as the survivor in this run
                max_time_in_run = max(max_time_in_run, neededTime[i])
            else:
                # New color run starts
                max_time_in_run = neededTime[i]

        return total
