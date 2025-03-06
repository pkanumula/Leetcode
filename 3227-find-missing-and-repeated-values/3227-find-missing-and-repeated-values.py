from typing import List

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        total_elements = n * n
        expected_sum = total_elements * (total_elements + 1) // 2
        actual_sum = 0
        seen = set()
        repeated = -1

        for row in grid:
            for num in row:
                if num in seen:
                    repeated = num
                seen.add(num)
                actual_sum += num

        missing = expected_sum - (actual_sum - repeated)

        return [repeated, missing]
