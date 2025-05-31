from collections import deque
from typing import List

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)

        def get_coordinates(label):
            # Get row and column for a given square label (1-indexed)
            row = n - 1 - (label - 1) // n
            col = (label - 1) % n
            if (n - 1 - row) % 2 == 1:  # reverse direction for every other row
                col = n - 1 - col
            return row, col

        visited = set()
        queue = deque([(1, 0)])  # (square label, moves)

        while queue:
            curr, moves = queue.popleft()
            for i in range(1, 7):  # simulate die roll
                next_square = curr + i
                if next_square > n * n:
                    continue
                r, c = get_coordinates(next_square)
                if board[r][c] != -1:
                    next_square = board[r][c]
                if next_square == n * n:
                    return moves + 1
                if next_square not in visited:
                    visited.add(next_square)
                    queue.append((next_square, moves + 1))
        return -1
