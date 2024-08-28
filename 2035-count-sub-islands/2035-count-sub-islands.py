class Solution(object):
    def countSubIslands(self, grid1, grid2):
        """
        :type grid1: List[List[int]]
        :type grid2: List[List[int]]
        :rtype: int
        """
        
        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid2[i][j] == 0:
                return True
            
            grid2[i][j] = 0  # Mark visited
            is_sub_island = grid1[i][j] == 1
            
            # Explore all four directions
            is_sub_island &= dfs(i + 1, j)
            is_sub_island &= dfs(i - 1, j)
            is_sub_island &= dfs(i, j + 1)
            is_sub_island &= dfs(i, j - 1)
            
            return is_sub_island
        
        m, n = len(grid1), len(grid2[0])
        count = 0
        
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1 and dfs(i, j):
                    count += 1
        
        return count
