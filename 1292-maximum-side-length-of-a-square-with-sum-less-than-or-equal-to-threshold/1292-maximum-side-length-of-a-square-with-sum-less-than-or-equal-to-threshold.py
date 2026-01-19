from typing import List

class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])

        # Build prefix sum array (m+1) x (n+1)
        prefix = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            row_sum = 0
            for j in range(1, n + 1):
                row_sum += mat[i - 1][j - 1]
                prefix[i][j] = prefix[i - 1][j] + row_sum

        # Helper: check if there exists a k x k square with sum <= threshold
        def possible(k: int) -> bool:
            for i in range(k, m + 1):
                for j in range(k, n + 1):
                    total = (prefix[i][j]
                             - prefix[i - k][j]
                             - prefix[i][j - k]
                             + prefix[i - k][j - k])
                    if total <= threshold:
                        return True
            return False

        # Binary search on side length
        low, high = 0, min(m, n)
        while low < high:
            mid = (low + high + 1) // 2
            if possible(mid):
                low = mid
            else:
                high = mid - 1

        return low
