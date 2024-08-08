class Solution(object):
    def spiralMatrixIII(self, rows, cols, rStart, cStart):
        """
        :type rows: int
        :type cols: int
        :type rStart: int
        :type cStart: int
        :rtype: List[List[int]]
        """
        result = [[rStart, cStart]]
        if rows * cols == 1:
            return result
        
        # Directions: east, south, west, north
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        step = 1
        
        r, c = rStart, cStart
        
        while len(result) < rows * cols:
            for dx, dy in directions:
                for _ in range(step):
                    r += dx
                    c += dy
                    if 0 <= r < rows and 0 <= c < cols:
                        result.append([r, c])
                    if len(result) == rows * cols:
                        return result
                if dx != 0:  # Increase steps after moving north or south
                    step += 1

        return result
