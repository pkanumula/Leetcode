class Solution:
    def gridGame(self, grid: list[list[int]]) -> int:
        n = len(grid[0])

        # Prefix sums for the two rows
        top_prefix = [0] * n
        bottom_prefix = [0] * n

        # Calculate prefix sums for the top row
        top_prefix[0] = grid[0][0]
        for i in range(1, n):
            top_prefix[i] = top_prefix[i - 1] + grid[0][i]

        # Calculate prefix sums for the bottom row
        bottom_prefix[0] = grid[1][0]
        for i in range(1, n):
            bottom_prefix[i] = bottom_prefix[i - 1] + grid[1][i]

        # Initialize the minimum points collected by the second robot
        result = float('inf')

        for i in range(n):
            # Points left for the second robot if the first robot cuts at column i
            top_remaining = top_prefix[n - 1] - top_prefix[i]
            bottom_remaining = bottom_prefix[i - 1] if i > 0 else 0

            # The second robot will take the maximum of the two remaining segments
            second_robot_points = max(top_remaining, bottom_remaining)

            # Update the result to minimize the second robot's points
            result = min(result, second_robot_points)

        return result
