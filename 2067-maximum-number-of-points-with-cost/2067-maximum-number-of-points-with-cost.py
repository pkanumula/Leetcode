class Solution:
    def maxPoints(self, points):
        m, n = len(points), len(points[0])
        
        # Initialize the previous row DP array with the values of the first row
        prev_dp = points[0][:]
        
        # Iterate over each row starting from the second row
        for i in range(1, m):
            # Left to right pass: compute the best score we can get considering left cells
            left = [0] * n
            left[0] = prev_dp[0]
            for j in range(1, n):
                left[j] = max(left[j - 1], prev_dp[j] + j)
            
            # Right to left pass: compute the best score we can get considering right cells
            right = [0] * n
            right[n - 1] = prev_dp[n - 1] - (n - 1)
            for j in range(n - 2, -1, -1):
                right[j] = max(right[j + 1], prev_dp[j] - j)
            
            # Update the current row DP array using the max values from left and right
            curr_dp = [0] * n
            for j in range(n):
                curr_dp[j] = points[i][j] + max(left[j] - j, right[j] + j)
            
            # Move to the next row
            prev_dp = curr_dp
        
        # The answer is the maximum value in the last DP array
        return max(prev_dp)
