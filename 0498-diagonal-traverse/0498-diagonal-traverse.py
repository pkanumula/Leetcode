class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []

        m, n = len(mat), len(mat[0])
        result = []
        r, c = 0, 0
        direction = 1  # 1 = up-right, -1 = down-left

        for _ in range(m * n):
            result.append(mat[r][c])

            if direction == 1:  # moving up-right
                if c == n - 1:  # last column, go down
                    r += 1
                    direction = -1
                elif r == 0:  # first row, go right
                    c += 1
                    direction = -1
                else:
                    r -= 1
                    c += 1
            else:  # moving down-left
                if r == m - 1:  # last row, go right
                    c += 1
                    direction = 1
                elif c == 0:  # first column, go down
                    r += 1
                    direction = 1
                else:
                    r += 1
                    c -= 1

        return result
