class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        blanks = moves.count('_')
        left = moves.count('L')
        right = moves.count('R')
        return abs(left - right) + blanks