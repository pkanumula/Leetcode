class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        from collections import defaultdict

        # Map to store the position of each number in the matrix
        position_map = {}
        for i, row in enumerate(mat):
            for j, val in enumerate(row):
                position_map[val] = (i, j)

        # Initialize row and column paint counters
        m, n = len(mat), len(mat[0])
        row_count = [0] * m
        col_count = [0] * n

        # Iterate through arr and paint cells
        for i, num in enumerate(arr):
            r, c = position_map[num]
            row_count[r] += 1
            col_count[c] += 1

            # Check if the row or column is completely painted
            if row_count[r] == n or col_count[c] == m:
                return i

        return -1