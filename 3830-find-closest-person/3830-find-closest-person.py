class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        dist1 = abs(x - z)  # distance Person 1 needs to travel
        dist2 = abs(y - z)  # distance Person 2 needs to travel

        if dist1 < dist2:
            return 1
        elif dist2 < dist1:
            return 2
        else:
            return 0
