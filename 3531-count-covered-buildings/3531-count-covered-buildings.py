from typing import List
from collections import defaultdict

class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        # Dictionaries to track min/max y for each row x
        row_min = {}
        row_max = {}
        # Dictionaries to track min/max x for each column y
        col_min = {}
        col_max = {}
        
        # First pass: compute extremes for each row and column
        for x, y in buildings:
            if x not in row_min:
                row_min[x] = row_max[x] = y
            else:
                if y < row_min[x]:
                    row_min[x] = y
                if y > row_max[x]:
                    row_max[x] = y
            
            if y not in col_min:
                col_min[y] = col_max[y] = x
            else:
                if x < col_min[y]:
                    col_min[y] = x
                if x > col_max[y]:
                    col_max[y] = x
        
        # Second pass: count covered buildings
        covered = 0
        for x, y in buildings:
            # Check if (x, y) is not at the extremes in its row and column
            if row_min[x] < y < row_max[x] and col_min[y] < x < col_max[y]:
                covered += 1
        
        return covered
