from typing import List
from collections import defaultdict

class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        events = defaultdict(int)  # y -> change in slope
        total = 0

        for x, y, l in squares:
            events[y] += l
            events[y + l] -= l
            total += l * l

        target = total  # we'll compare 2*area_below against total (avoids fractions)
        ys = sorted(events.keys())

        cur = ys[0]
        slope = events[cur]  # slope on (cur, next_y)
        area_below = 0       # area below at height cur

        for ny in ys[1:]:
            dy = ny - cur

            # If already exactly half at the lowest possible y in this interval
            if 2 * area_below == target:
                return float(cur)

            if slope > 0 and dy > 0:
                add = slope * dy  # area gained over (cur, ny)
                if 2 * (area_below + add) >= target:
                    # Solve: area_below + slope*(t-cur) = total/2
                    rem = target - 2 * area_below
                    return float(cur + rem / (2.0 * slope))
                area_below += add

            cur = ny
            slope += events[cur]

        # If it hits exactly at the last event height
        if 2 * area_below == target:
            return float(cur)

        # Shouldn't be needed, but keep a safe fallback
        return float(cur)
