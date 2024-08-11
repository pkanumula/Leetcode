class Solution:
    def minDays(self, grid):
        if self.isDisconnected(grid):
            return 0
        if self.canDisconnectInOneMove(grid):
            return 1
        return 2

    def isDisconnected(self, grid):
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        land_cells = sum(cell for row in grid for cell in row)

        def dfs(x, y):
            if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == 0 or visited[x][y]:
                return 0
            visited[x][y] = True
            return 1 + dfs(x + 1, y) + dfs(x - 1, y) + dfs(x, y + 1) + dfs(x, y - 1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    connected_land = dfs(i, j)
                    return connected_land != land_cells
        return True

    def canDisconnectInOneMove(self, grid):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    if self.isDisconnected(grid):
                        return True
                    grid[i][j] = 1
        return False
