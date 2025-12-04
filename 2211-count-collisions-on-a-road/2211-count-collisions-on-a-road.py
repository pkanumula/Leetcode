class Solution:
    def countCollisions(self, directions: str) -> int:
        n = len(directions)
        
        # Skip all leading 'L' cars – they move left forever without colliding
        left = 0
        while left < n and directions[left] == 'L':
            left += 1
        
        # Skip all trailing 'R' cars – they move right forever without colliding
        right = n - 1
        while right >= 0 and directions[right] == 'R':
            right -= 1
        
        # Now, in directions[left:right+1], every 'L' or 'R' must collide once
        collisions = 0
        for i in range(left, right + 1):
            if directions[i] != 'S':
                collisions += 1
        
        return collisions
