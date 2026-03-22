class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        # Helper function to rotate matrix 90 degrees clockwise
        def rotate_90(matrix):
            n = len(matrix)
            # Transpose the matrix
            for i in range(n):
                for j in range(i + 1, n):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

            # Reverse each row
            for i in range(n):
                matrix[i].reverse()

            return matrix

        # Helper function to check if two matrices are equal
        def matrices_equal(m1, m2):
            for i in range(len(m1)):
                if m1[i] != m2[i]:
                    return False
            return True

        # Check if mat equals target in any of 4 rotations
        for _ in range(4):
            if matrices_equal(mat, target):
                return True
            rotate_90(mat)

        return False