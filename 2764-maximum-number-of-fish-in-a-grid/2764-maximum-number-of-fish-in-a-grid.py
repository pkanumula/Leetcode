from typing import List

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        def dfs(r, c):
            # If out of bounds or cell is land (0), stop exploration
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == 0:
                return 0
            
            fish = grid[r][c]  # Catch fish in the current cell
            grid[r][c] = 0  # Mark the cell as visited
            
            # Explore all adjacent cells
            for dr, dc in directions:
                fish += dfs(r + dr, c + dc)
            
            return fish
        
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        max_fish = 0
        
        # Start DFS from each water cell
        for r in range(m):
            for c in range(n):
                if grid[r][c] > 0:  # Only start from water cells
                    max_fish = max(max_fish, dfs(r, c))
        
        return max_fish