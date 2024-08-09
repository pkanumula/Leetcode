class Solution(object):
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def isMagic(a, b, c, d, e, f, g, h, i):
            return sorted([a, b, c, d, e, f, g, h, i]) == list(range(1, 10)) and \
                   (a + b + c == d + e + f == g + h + i == a + d + g == b + e + h == c + f + i == a + e + i == c + e + g == 15)

        rows, cols = len(grid), len(grid[0])
        count = 0
        
        for r in range(rows - 2):
            for c in range(cols - 2):
                if grid[r+1][c+1] == 5 and isMagic(grid[r][c], grid[r][c+1], grid[r][c+2],
                                                    grid[r+1][c], grid[r+1][c+1], grid[r+1][c+2],
                                                    grid[r+2][c], grid[r+2][c+1], grid[r+2][c+2]):
                    count += 1
                    
        return count
