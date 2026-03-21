class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        """
        Flip a k×k square submatrix starting at (x, y) by reversing rows vertically.

        Args:
            grid: m×n integer matrix
            x: row index of top-left corner
            y: column index of top-left corner
            k: size of the square submatrix

        Returns:
            Updated matrix with the submatrix flipped vertically
        """
        # Swap rows from top and bottom of the submatrix
        for i in range(k // 2):
            # Current top row index and corresponding bottom row index
            top_row = x + i
            bottom_row = x + k - 1 - i

            # Swap the rows (including only the submatrix columns)
            for j in range(y, y + k):
                grid[top_row][j], grid[bottom_row][j] = grid[bottom_row][j], grid[top_row][j]

        return grid