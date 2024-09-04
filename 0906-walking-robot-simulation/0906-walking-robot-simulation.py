class Solution(object):
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        # Directions: North, East, South, West
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        # Start at origin facing North
        x, y = 0, 0
        direction_idx = 0  # 0 = North, 1 = East, 2 = South, 3 = West
        max_distance_squared = 0
        
        # Convert obstacles list to a set of tuples for O(1) access
        obstacle_set = set(map(tuple, obstacles))
        
        for command in commands:
            if command == -2:  # Turn left
                direction_idx = (direction_idx - 1) % 4
            elif command == -1:  # Turn right
                direction_idx = (direction_idx + 1) % 4
            else:
                dx, dy = directions[direction_idx]
                for _ in range(command):
                    # Check the next position
                    if (x + dx, y + dy) not in obstacle_set:
                        x += dx
                        y += dy
                        # Calculate squared distance from origin
                        max_distance_squared = max(max_distance_squared, x * x + y * y)
                    else:
                        break
        
        return max_distance_squared
