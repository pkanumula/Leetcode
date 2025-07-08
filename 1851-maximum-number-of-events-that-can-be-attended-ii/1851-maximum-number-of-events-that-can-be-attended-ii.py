from bisect import bisect_left
from functools import lru_cache

class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        # Sort events by start day to use binary search for next event
        events.sort()
        n = len(events)

        # Precompute start days for binary search
        start_days = [event[0] for event in events]

        @lru_cache(None)
        def dp(index: int, remaining: int) -> int:
            if index == n or remaining == 0:
                return 0

            # Option 1: skip current event
            skip = dp(index + 1, remaining)

            # Option 2: take current event and jump to next non-overlapping
            _, end, value = events[index]
            # Find first event that starts after 'end'
            next_index = bisect_left(start_days, end + 1)
            take = value + dp(next_index, remaining - 1)

            return max(skip, take)

        return dp(0, k)
