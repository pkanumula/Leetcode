class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        rhombus_sums = set()

        # Iterate through each cell as a potential rhombus center
        for i in range(m):
            for j in range(n):
                # Case 1: Rhombus with area 0 (just the center cell)
                rhombus_sums.add(grid[i][j])

                # Case 2: Rhombus with increasing radius
                radius = 1
                while True:
                    # Check if rhombus fits in grid
                    if i - radius < 0 or i + radius >= m or j - radius < 0 or j + radius >= n:
                        break

                    # Calculate the sum of the rhombus border
                    rhombus_sum = 0

                    # Top corner to right corner (going down-right)
                    for k in range(radius + 1):
                        rhombus_sum += grid[i - radius + k][j + k]

                    # Right corner to bottom corner (going down-left, excluding right corner)
                    for k in range(1, radius + 1):
                        rhombus_sum += grid[i + k][j + radius - k]

                    # Bottom corner to left corner (going up-left, excluding bottom corner)
                    for k in range(1, radius + 1):
                        rhombus_sum += grid[i + radius - k][j - k]

                    # Left corner to top corner (going up-right, excluding both endpoints)
                    for k in range(1, radius):
                        rhombus_sum += grid[i - k][j - radius + k]

                    rhombus_sums.add(rhombus_sum)
                    radius += 1

        # Sort sums in descending order and return top 3
        sorted_sums = sorted(rhombus_sums, reverse=True)
        return sorted_sums[:3]