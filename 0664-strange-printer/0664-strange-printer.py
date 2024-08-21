class Solution(object):
    def strangePrinter(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        
        for i in range(n):
            dp[i][i] = 1  # A single character needs only one turn to print
        
        for length in range(2, n+1):  # Length of substring
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = dp[i + 1][j] + 1  # Start with one additional print turn
                for k in range(i + 1, j + 1):
                    if s[k] == s[i]:
                        if k == j:
                            dp[i][j] = min(dp[i][j], dp[i][k-1])
                        else:
                            dp[i][j] = min(dp[i][j], dp[i][k-1] + dp[k+1][j])
        
        return dp[0][n-1]
