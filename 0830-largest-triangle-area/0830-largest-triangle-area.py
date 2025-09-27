from typing import List
from itertools import combinations

class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        def area(a, b, c) -> float:
            (x1, y1), (x2, y2), (x3, y3) = a, b, c
            # 2 * area = |(x2 - x1)(y3 - y1) - (x3 - x1)(y2 - y1)|
            return abs((x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)) / 2.0

        max_area = 0.0
        for a, b, c in combinations(points, 3):
            max_area = max(max_area, area(a, b, c))
        return max_area
