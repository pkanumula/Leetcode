class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        # Convert obstacles to a set for O(1) lookup
        obstacle_set = set(map(tuple, obstacles))

        # Direction vectors: North, East, South, West
        # Index 0: North (0, 1), 1: East (1, 0), 2: South (0, -1), 3: West (-1, 0)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        # Start position and direction
        x, y = 0, 0
        direction_idx = 0  # Start facing North

        max_distance_sq = 0

        for command in commands:
            if command == -2:  # Turn left
                direction_idx = (direction_idx - 1) % 4
            elif command == -1:  # Turn right
                direction_idx = (direction_idx + 1) % 4
            else:  # Move forward k units
                dx, dy = directions[direction_idx]
                # Move one unit at a time to handle obstacles
                for _ in range(command):
                    # Check if next position has an obstacle
                    next_x, next_y = x + dx, y + dy

                    # Don't move if obstacle exists (except at origin during first move)
                    if (next_x, next_y) not in obstacle_set:
                        x, y = next_x, next_y
                    else:
                        break  # Stop moving in this direction

            # Update maximum squared distance
            max_distance_sq = max(max_distance_sq, x * x + y * y)

        return max_distance_sq