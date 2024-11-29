import heapq
from typing import List

class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        # Early exit if initial movement isn't possible
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = [[False] * n for _ in range(m)]
        heap = [(0, 0, 0)]  # (time, row, col)

        while heap:
            time, row, col = heapq.heappop(heap)
            
            # If we've reached the bottom-right corner, return the time
            if (row, col) == (m - 1, n - 1):
                return time
            
            if visited[row][col]:
                continue
            visited[row][col] = True

            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
                    required_time = grid[nr][nc]
                    
                    # Wait time calculation
                    if time + 1 < required_time:
                        wait_time = required_time - (time + 1)
                        if wait_time % 2 == 1:  # Align to even timestamp
                            wait_time += 1
                        next_time = time + 1 + wait_time
                    else:
                        next_time = time + 1
                    
                    heapq.heappush(heap, (next_time, nr, nc))
        
        return -1  # No valid path exists
