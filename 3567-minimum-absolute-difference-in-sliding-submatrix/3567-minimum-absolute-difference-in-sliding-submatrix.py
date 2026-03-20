from typing import List

class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        result = []

        for i in range(m - k + 1):
            row_result = []

            for j in range(n - k + 1):
                # Get distinct values in k x k submatrix
                values = set()
                for x in range(i, i + k):
                    for y in range(j, j + k):
                        values.add(grid[x][y])

                # Convert to sorted list
                sorted_values = sorted(values)

                # Find minimum absolute difference
                min_diff = float('inf')
                for idx in range(len(sorted_values) - 1):
                    min_diff = min(min_diff, sorted_values[idx + 1] - sorted_values[idx])

                row_result.append(0 if min_diff == float('inf') else min_diff)

            result.append(row_result)

        return result