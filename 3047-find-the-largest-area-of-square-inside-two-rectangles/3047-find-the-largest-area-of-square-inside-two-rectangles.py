from typing import List

class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        n = len(bottomLeft)
        ans = 0

        for i in range(n):
            ax1, ay1 = bottomLeft[i]
            ax2, ay2 = topRight[i]

            for j in range(i + 1, n):
                bx1, by1 = bottomLeft[j]
                bx2, by2 = topRight[j]

                # intersection rectangle
                inter_w = min(ax2, bx2) - max(ax1, bx1)
                inter_h = min(ay2, by2) - max(ay1, by1)

                if inter_w > 0 and inter_h > 0:
                    side = min(inter_w, inter_h)
                    ans = max(ans, side * side)

        return ans
