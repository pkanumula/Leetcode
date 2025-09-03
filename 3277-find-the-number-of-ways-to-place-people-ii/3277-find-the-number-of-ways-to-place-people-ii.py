from typing import List
import bisect

class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        # Sort by x asc, y desc (important for same-x vertical fences)
        pts = sorted(points, key=lambda p: (p[0], -p[1]))
        n = len(pts)
        ans = 0

        for i in range(n):
            yi = pts[i][1]
            S = []  # sorted list of y's for indices strictly between i and j
            for j in range(i + 1, n):
                yj = pts[j][1]
                if yi >= yj:
                    # check if any y in between falls into [yj, yi]
                    k = bisect.bisect_left(S, yj)
                    ok = True
                    if k < len(S) and S[k] <= yi:
                        ok = False
                    if ok:
                        ans += 1
                bisect.insort(S, yj)
        return ans
