from typing import List

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # dp[i][j] = best count using at most i zeros and j ones
        dp = [[0]*(n+1) for _ in range(m+1)]

        for s in strs:
            zeros = s.count('0')
            ones = len(s) - zeros

            # reverse iterate to enforce 0/1 (each string at most once)
            for i in range(m, zeros-1, -1):
                for j in range(n, ones-1, -1):
                    dp[i][j] = max(dp[i][j], dp[i-zeros][j-ones] + 1)

        return dp[m][n]
