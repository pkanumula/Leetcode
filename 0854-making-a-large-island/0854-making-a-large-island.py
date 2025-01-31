from typing import List

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        island_id = 2  # Start with an ID of 2 to avoid confusion with 0s and 1s
        island_sizes = {0: 0}  # Dictionary to track sizes of each island

        # Helper function to perform DFS and calculate island size
        def dfs(r, c, id):
            if r < 0 or r >= n or c < 0 or c >= n or grid[r][c] != 1:
                return 0
            grid[r][c] = id
            size = 1
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                size += dfs(r + dr, c + dc, id)
            return size

        # Step 1: Identify all islands and calculate their sizes
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    island_sizes[island_id] = dfs(r, c, island_id)
                    island_id += 1

        # Step 2: Check each 0 in the grid and calculate the largest possible island size
        max_island = max(island_sizes.values(), default=0)

        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:
                    seen = set()
                    potential_size = 1
                    for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] > 1:
                            root = grid[nr][nc]
                            if root not in seen:
                                seen.add(root)
                                potential_size += island_sizes[root]
                    max_island = max(max_island, potential_size)

        return max_island
