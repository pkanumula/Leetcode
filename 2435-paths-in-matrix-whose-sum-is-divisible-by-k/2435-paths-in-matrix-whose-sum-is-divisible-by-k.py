from typing import List

class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])

        # prev[j][r] = number of paths to cell (current_row-1, j) with remainder r
        prev = [[0] * k for _ in range(n)]

        # Initialize first cell (0, 0)
        first_rem = grid[0][0] % k
        prev[0][first_rem] = 1

        # Fill first row (only from the left)
        for j in range(1, n):
            val = grid[0][j] % k
            for r in range(k):
                cnt = prev[j - 1][r]
                if cnt:
                    nr = (r + val) % k
                    prev[j][nr] = (prev[j][nr] + cnt) % MOD

        # Process remaining rows
        for i in range(1, m):
            curr = [[0] * k for _ in range(n)]

            # First column in this row (only from top)
            val = grid[i][0] % k
            for r in range(k):
                cnt = prev[0][r]
                if cnt:
                    nr = (r + val) % k
                    curr[0][nr] = (curr[0][nr] + cnt) % MOD

            # Other columns: from top and left
            for j in range(1, n):
                val = grid[i][j] % k
                for r in range(k):
                    total = prev[j][r] + curr[j - 1][r]
                    if total:
                        nr = (r + val) % k
                        curr[j][nr] = (curr[j][nr] + total) % MOD

            prev = curr

        # We want paths ending at (m-1, n-1) with sum % k == 0
        return prev[n - 1][0]
