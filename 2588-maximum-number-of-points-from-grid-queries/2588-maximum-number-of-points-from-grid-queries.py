from heapq import heappush, heappop
from typing import List

class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        m, n = len(grid), len(grid[0])
        queries_sorted = sorted(enumerate(queries), key=lambda x: x[1])
        res = [0] * len(queries)

        heap = [(grid[0][0], 0, 0)]  # Min-heap with (value, x, y)
        visited = set()
        visited.add((0, 0))

        count = 0

        for idx, q in queries_sorted:
            while heap and heap[0][0] < q:
                val, x, y = heappop(heap)
                count += 1  # Gain a point for visiting this cell

                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited:
                        visited.add((nx, ny))
                        heappush(heap, (grid[nx][ny], nx, ny))

            res[idx] = count

        return res
