from typing import List

class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        
        # heights[j] will store the consecutive count of 1s column-wise
        heights = [0] * n
        total = 0
        
        for i in range(m):
            # Update histogram heights for this row
            for j in range(n):
                if mat[i][j] == 0:
                    heights[j] = 0
                else:
                    heights[j] += 1
            
            # Count submatrices ending at this row using heights
            stack = []
            sum_in_row = 0
            for j in range(n):
                count = 1
                while stack and stack[-1][0] >= heights[j]:
                    h, c = stack.pop()
                    sum_in_row -= h * c
                    count += c
                stack.append((heights[j], count))
                sum_in_row += heights[j] * count
                total += sum_in_row
        
        return total
