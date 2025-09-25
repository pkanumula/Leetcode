from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        # dp holds the best sums from the current row to the bottom
        dp = triangle[-1][:]  # copy last row; size = n

        # Work upward: each dp[c] becomes best path sum starting at (r, c)
        for r in range(n - 2, -1, -1):
            for c in range(r + 1):
                dp[c] = triangle[r][c] + min(dp[c], dp[c + 1])

        return dp[0]
