from typing import List

class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        # 0 = empty, 1 = wall, 2 = guard, 3 = guarded
        grid = [[0]*n for _ in range(m)]
        for r, c in walls:
            grid[r][c] = 1
        for r, c in guards:
            grid[r][c] = 2

        # Row sweeps
        for r in range(m):
            seen = False
            for c in range(n):  # left -> right
                if grid[r][c] == 1:
                    seen = False
                elif grid[r][c] == 2:
                    seen = True
                elif seen and grid[r][c] == 0:
                    grid[r][c] = 3
            seen = False
            for c in range(n-1, -1, -1):  # right -> left
                if grid[r][c] == 1:
                    seen = False
                elif grid[r][c] == 2:
                    seen = True
                elif seen and grid[r][c] == 0:
                    grid[r][c] = 3

        # Column sweeps
        for c in range(n):
            seen = False
            for r in range(m):  # top -> bottom
                if grid[r][c] == 1:
                    seen = False
                elif grid[r][c] == 2:
                    seen = True
                elif seen and grid[r][c] == 0:
                    grid[r][c] = 3
            seen = False
            for r in range(m-1, -1, -1):  # bottom -> top
                if grid[r][c] == 1:
                    seen = False
                elif grid[r][c] == 2:
                    seen = True
                elif seen and grid[r][c] == 0:
                    grid[r][c] = 3

        # Count unguarded, unoccupied cells
        ans = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    ans += 1
        return ans
