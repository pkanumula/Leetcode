from collections import deque

class Solution:
    def slidingPuzzle(self, board: list[list[int]]) -> int:
        # Convert the board into a string for easy manipulation
        start = ''.join(str(num) for row in board for num in row)
        target = "123450"
        
        # Possible moves for each position on the board
        neighbors = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4],
            4: [1, 3, 5],
            5: [2, 4]
        }
        
        # BFS setup
        queue = deque([(start, start.index('0'), 0)])  # (current state, index of 0, moves)
        visited = set()
        visited.add(start)
        
        while queue:
            state, zero_idx, moves = queue.popleft()
            
            if state == target:
                return moves
            
            # Explore neighbors
            for neighbor in neighbors[zero_idx]:
                # Create a new state by swapping 0 with its neighbor
                new_state = list(state)
                new_state[zero_idx], new_state[neighbor] = new_state[neighbor], new_state[zero_idx]
                new_state = ''.join(new_state)
                
                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, neighbor, moves + 1))
        
        # If target state is not reachable
        return -1
