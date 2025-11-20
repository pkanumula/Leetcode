from typing import List

class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        # Sort by end asc, and if tie, start desc
        intervals.sort(key=lambda x: (x[1], -x[0]))

        # p1 < p2: the two largest chosen points so far
        p1, p2 = -1, -1
        ans = 0

        for a, b in intervals:
            count = 0
            if p1 >= a and p1 <= b:
                count += 1
            if p2 >= a and p2 <= b:
                count += 1

            if count >= 2:
                # interval already has 2 points from our set
                continue
            elif count == 1:
                # add one more point: b
                ans += 1
                # shift: p1 becomes the previous p2 (which is inside),
                # p2 becomes the new point b
                p1, p2 = p2, b
            else:
                # add two points: b-1 and b
                ans += 2
                p1, p2 = b - 1, b

        return ans
