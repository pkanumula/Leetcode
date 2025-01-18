from collections import deque

class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        # Directions based on the signs
        directions = {
            1: (0, 1),   # right
            2: (0, -1),  # left
            3: (1, 0),   # down
            4: (-1, 0)   # up
        }

        m, n = len(grid), len(grid[0])
        cost = [[float('inf')] * n for _ in range(m)]
        cost[0][0] = 0

        dq = deque([(0, 0, 0)])  # (current_cost, row, col)

        while dq:
            c, x, y = dq.popleft()

            # Skip if the current path is not optimal
            if c > cost[x][y]:
                continue

            for direction, (dx, dy) in directions.items():
                nx, ny = x + dx, y + dy
                new_cost = c + (1 if grid[x][y] != direction else 0)

                if 0 <= nx < m and 0 <= ny < n and new_cost < cost[nx][ny]:
                    cost[nx][ny] = new_cost
                    if grid[x][y] == direction:
                        dq.appendleft((new_cost, nx, ny))  # Prioritize no-cost moves
                    else:
                        dq.append((new_cost, nx, ny))

        return cost[m-1][n-1]