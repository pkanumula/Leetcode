from typing import List
import bisect

class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        def to_perimeter(x, y):
            if y == 0:      return x
            elif x == side: return side + y
            elif y == side: return 2 * side + (side - x)
            else:           return 3 * side + (side - y)
        
        perim = sorted(to_perimeter(x, y) for x, y in points)
        n = len(perim)
        total = 4 * side
        # Doubled array for circular handling
        perim2 = perim + [p + total for p in perim]
        
        def can_place(min_dist: int) -> bool:
            # For each starting point, greedily pick k points using bisect
            for start in range(n):
                count = 1
                last = perim2[start]
                pos = start
                while count < k:
                    # Find next point at distance >= min_dist from last
                    need = last + min_dist
                    # Search only within [start, start+n)
                    idx = bisect.bisect_left(perim2, need, pos + 1, start + n)
                    if idx >= start + n:
                        break  # Can't place more points
                    last = perim2[idx]
                    pos = idx
                    count += 1
                
                if count == k:
                    # Check wrap-around: distance from last back to start
                    wrap = (perim2[start] + total) - last
                    if wrap >= min_dist:
                        return True
            return False
        
        lo, hi = 1, 2 * side
        ans = 0
        while lo <= hi:
            mid = (lo + hi) // 2
            if can_place(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        
        return ans