from typing import List
import heapq

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        # Edge cases: too thin to hold water
        if not heightMap or not heightMap[0]:
            return 0
        m, n = len(heightMap), len(heightMap[0])
        if m < 3 or n < 3:
            return 0

        visited = [[False]*n for _ in range(m)]
        heap = []  # (height, r, c)

        # 1) Push all boundary cells into the heap (they form the initial "walls")
        for r in range(m):
            for c in (0, n-1):
                heapq.heappush(heap, (heightMap[r][c], r, c))
                visited[r][c] = True
        for c in range(n):
            for r in (0, m-1):
                if not visited[r][c]:
                    heapq.heappush(heap, (heightMap[r][c], r, c))
                    visited[r][c] = True

        # 2) Pop the lowest wall, try to expand to neighbors
        water = 0
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        while heap:
            h, r, c = heapq.heappop(heap)
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
                    visited[nr][nc] = True
                    nh = heightMap[nr][nc]
                    # If neighbor is lower than current wall height, it can trap water
                    if nh < h:
                        water += h - nh
                        # Push with wall height h (water level becomes the new wall)
                        heapq.heappush(heap, (h, nr, nc))
                    else:
                        # No water trapped; neighbor becomes a new wall of height nh
                        heapq.heappush(heap, (nh, nr, nc))

        return water
