class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        
        def dfs(row, col, prev_row, prev_col, char):
            visited[row][col] = True
            
            for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                nr, nc = row + dr, col + dc
                
                # Skip out of bounds or different characters
                if nr < 0 or nr >= m or nc < 0 or nc >= n:
                    continue
                if grid[nr][nc] != char:
                    continue
                
                # Skip the cell we just came from (no immediate backtrack)
                if nr == prev_row and nc == prev_col:
                    continue
                
                # If already visited → cycle found
                if visited[nr][nc]:
                    return True
                
                if dfs(nr, nc, row, col, char):
                    return True
            
            return False
        
        for i in range(m):
            for j in range(n):
                if not visited[i][j]:
                    if dfs(i, j, -1, -1, grid[i][j]):
                        return True
        
        return False