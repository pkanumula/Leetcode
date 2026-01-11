from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        heights = [0] * cols
        best = 0

        for r in range(rows):
            # Build/update histogram heights for this row
            for c in range(cols):
                if matrix[r][c] == '1':
                    heights[c] += 1
                else:
                    heights[c] = 0

            # Largest rectangle in histogram (monotonic stack)
            stack = []  # stores indices with increasing heights
            for i in range(cols + 1):
                cur_h = heights[i] if i < cols else 0  # sentinel to flush stack
                while stack and cur_h < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    left_smaller = stack[-1] if stack else -1
                    width = i - left_smaller - 1
                    best = max(best, h * width)
                stack.append(i)

        return best
