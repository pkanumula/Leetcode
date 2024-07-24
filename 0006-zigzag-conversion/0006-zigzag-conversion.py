class Solution(object):
    def convert(self, s, numRows):
        # If numRows is 1, no zigzag pattern can be formed
        if numRows == 1 or numRows >= len(s):
            return s
        
        # Create an array to hold the strings for each row
        rows = [''] * numRows
        current_row = 0
        direction = -1
        
        for char in s:
            rows[current_row] += char
            # Change direction when we reach the top or bottom row
            if current_row == 0 or current_row == numRows - 1:
                direction *= -1
            current_row += direction
        
        # Join all rows to get the final string
        return ''.join(rows)