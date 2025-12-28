from typing import List

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        r, c = 0, n - 1
        count = 0

        while r < m and c >= 0:
            if grid[r][c] < 0:
                count += (m - r)   # all rows below (including r) are negative in this column
                c -= 1             # move left
            else:
                r += 1             # move down

        return count
