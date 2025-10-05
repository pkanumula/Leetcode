from collections import deque
from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        
        m, n = len(heights), len(heights[0])

        def bfs(starts):
            """BFS from a list of starting edge cells; move only to equal/higher neighbors."""
            q = deque(starts)
            seen = [[False]*n for _ in range(m)]
            for r, c in starts:
                seen[r][c] = True

            dirs = [(1,0), (-1,0), (0,1), (0,-1)]
            while q:
                r, c = q.popleft()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if (
                        0 <= nr < m and 0 <= nc < n
                        and not seen[nr][nc]
                        and heights[nr][nc] >= heights[r][c]  # can flow back “uphill”
                    ):
                        seen[nr][nc] = True
                        q.append((nr, nc))
            return seen

        # Pacific: top row & left col
        pacific_starts = [(0, c) for c in range(n)] + [(r, 0) for r in range(m)]
        pac = bfs(pacific_starts)

        # Atlantic: bottom row & right col
        atlantic_starts = [(m-1, c) for c in range(n)] + [(r, n-1) for r in range(m)]
        atl = bfs(atlantic_starts)

        # Cells reachable from both
        res = [[r, c] for r in range(m) for c in range(n) if pac[r][c] and atl[r][c]]
        return res
