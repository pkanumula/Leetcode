from typing import List

class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m, n = len(box), len(box[0])
        
        # Process each row to simulate gravity
        for row in box:
            empty = n - 1  # Start from the last column
            for col in range(n - 1, -1, -1):
                if row[col] == '#':  # Stone found
                    row[col], row[empty] = '.', '#'
                    empty -= 1
                elif row[col] == '*':  # Obstacle found
                    empty = col - 1
        
        # Rotate the box 90 degrees clockwise
        rotated_box = [[None] * m for _ in range(n)]
        for i in range(m):
            for j in range(n):
                rotated_box[j][m - 1 - i] = box[i][j]
        
        return rotated_box
