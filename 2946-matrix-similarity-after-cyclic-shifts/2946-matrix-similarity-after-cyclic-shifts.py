class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        m = len(mat)      # number of rows
        n = len(mat[0])   # number of columns

        # Optimize k using modulo - shifts repeat every n iterations
        k = k % n

        # If k becomes 0, no actual shift happens
        if k == 0:
            return True

        # Check each row
        for i in range(m):
            for j in range(n):
                if i % 2 == 0:  # Even-indexed row - left shift
                    # After left shift by k, element at position j comes from position (j + k) % n
                    if mat[i][j] != mat[i][(j + k) % n]:
                        return False
                else:  # Odd-indexed row - right shift
                    # After right shift by k, element at position j comes from position (j - k) % n
                    if mat[i][j] != mat[i][(j - k) % n]:
                        return False

        return True