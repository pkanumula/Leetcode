from typing import List

class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        # Difference matrix of size (n+1) x (n+1)
        diff = [[0] * (n + 1) for _ in range(n + 1)]
        
        # Apply 2D difference updates
        for r1, c1, r2, c2 in queries:
            diff[r1][c1] += 1
            if c2 + 1 <= n:
                diff[r1][c2 + 1] -= 1
            if r2 + 1 <= n:
                diff[r2 + 1][c1] -= 1
            if r2 + 1 <= n and c2 + 1 <= n:
                diff[r2 + 1][c2 + 1] += 1
        
        # Prefix sum over rows
        for i in range(n):
            running = 0
            for j in range(n):
                running += diff[i][j]
                diff[i][j] = running
        
        # Prefix sum over columns
        for j in range(n):
            running = 0
            for i in range(n):
                running += diff[i][j]
                diff[i][j] = running
        
        # Extract top-left n x n as the result matrix
        res = [row[:n] for row in diff[:n]]
        return res
