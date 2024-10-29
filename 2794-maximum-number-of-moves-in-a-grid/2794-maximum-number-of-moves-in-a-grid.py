from typing import List

class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[-1] * n for _ in range(m)]
        
        def dfs(row, col):
            if dp[row][col] != -1:
                return dp[row][col]
            
            max_moves = 0
            for dr, dc in [(-1, 1), (0, 1), (1, 1)]:
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < m and 0 <= new_col < n and grid[new_row][new_col] > grid[row][col]:
                    max_moves = max(max_moves, 1 + dfs(new_row, new_col))
            
            dp[row][col] = max_moves
            return max_moves

        result = 0
        for row in range(m):
            result = max(result, dfs(row, 0))
        
        return result
