from collections import Counter
from typing import List

class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        pattern_count = Counter()
        
        for row in matrix:
            # Create a normalized pattern by checking the first element
            normalized_pattern = tuple(cell ^ row[0] for cell in row)
            pattern_count[normalized_pattern] += 1
        
        # The maximum count of a normalized pattern is the result
        return max(pattern_count.values())
