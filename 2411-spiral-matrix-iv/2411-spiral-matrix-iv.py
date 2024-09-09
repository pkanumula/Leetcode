class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def spiralMatrix(self, m, n, head):
        """
        :type m: int
        :type n: int
        :type head: Optional[ListNode]
        :rtype: List[List[int]]
        """
        # Initialize the matrix with -1
        matrix = [[-1 for _ in range(n)] for _ in range(m)]
        
        # Define the directions for spiral order: right, down, left, up
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dir_idx = 0  # Start with the 'right' direction
        row, col = 0, 0
        
        # Iterate through the linked list
        current = head
        while current:
            # Place the value from the linked list in the matrix
            matrix[row][col] = current.val
            current = current.next
            
            # Calculate the next position
            next_row, next_col = row + directions[dir_idx][0], col + directions[dir_idx][1]
            
            # Check if the next position is out of bounds or already filled
            if next_row < 0 or next_row >= m or next_col < 0 or next_col >= n or matrix[next_row][next_col] != -1:
                # Change direction
                dir_idx = (dir_idx + 1) % 4
                next_row, next_col = row + directions[dir_idx][0], col + directions[dir_idx][1]
            
            # Move to the next position
            row, col = next_row, next_col
        
        return matrix
