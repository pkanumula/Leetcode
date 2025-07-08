from bisect import bisect_left
from functools import lru_cache
from typing import List

class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        # 1. sort by start day
        events.sort(key=lambda e: e[0])
        n = len(events)
        # 2. prepare an array of just the start days for binary search
        starts = [s for s, _, _ in events]

        # 3. nextIdx[i] = first event that starts strictly after events[i]'s end
        nextIdx = [bisect_left(starts, events[i][1] + 1) for i in range(n)]

        @lru_cache(maxsize=None)
        def dp(i: int, remaining: int) -> int:
            if i == n or remaining == 0:
                return 0
            # option 1: skip current
            best = dp(i + 1, remaining)
            # option 2: take current
            take = events[i][2] + dp(nextIdx[i], remaining - 1)
            return max(best, take)

        return dp(0, k)
