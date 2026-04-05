class Solution:
    def judgeCircle(self, moves: str) -> bool:
        # Count the occurrences of each move
        return moves.count('U') == moves.count('D') and moves.count('L') == moves.count('R')