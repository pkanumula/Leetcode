from typing import List
from collections import deque

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        # For each street type, which directions does it connect to?
        # Directions: 0=left, 1=right, 2=up, 3=down
        # (dr, dc, direction_from_current, required_direction_from_neighbor)
        # We define moves as (row_delta, col_delta, dir_needed_in_current, dir_needed_in_neighbor)
        
        # Streets that connect in each direction:
        connects = {
            1: {'left', 'right'},
            2: {'up', 'down'},
            3: {'left', 'down'},
            4: {'right', 'down'},
            5: {'left', 'up'},
            6: {'right', 'up'},
        }
        
        # opposite direction for the neighbor to "reach back"
        opposite = {'left': 'right', 'right': 'left', 'up': 'down', 'down': 'up'}
        
        # (row_delta, col_delta, direction_name)
        directions = [
            (0, -1, 'left'),
            (0,  1, 'right'),
            (-1, 0, 'up'),
            (1,  0, 'down'),
        ]
        
        visited = [[False] * n for _ in range(m)]
        queue = deque([(0, 0)])
        visited[0][0] = True
        
        while queue:
            r, c = queue.popleft()
            
            if r == m - 1 and c == n - 1:
                return True
            
            for dr, dc, direction in directions:
                nr, nc = r + dr, c + dc
                
                # Check bounds
                if not (0 <= nr < m and 0 <= nc < n):
                    continue
                
                # Check already visited
                if visited[nr][nc]:
                    continue
                
                # Current cell must connect toward this direction
                # Neighbor must connect back (opposite direction)
                if (direction in connects[grid[r][c]] and
                        opposite[direction] in connects[grid[nr][nc]]):
                    visited[nr][nc] = True
                    queue.append((nr, nc))
        
        return visited[m - 1][n - 1]