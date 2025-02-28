class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m, n = len(str1), len(str2)
        
        # Compute LCS using DP
        dp = [[""] * (n + 1) for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + str1[i - 1]
                else:
                    dp[i][j] = dp[i - 1][j] if len(dp[i - 1][j]) > len(dp[i][j - 1]) else dp[i][j - 1]

        # Construct shortest common supersequence using LCS
        i, j = 0, 0
        res = []
        for c in dp[m][n]:  
            while i < m and str1[i] != c:
                res.append(str1[i])
                i += 1
            while j < n and str2[j] != c:
                res.append(str2[j])
                j += 1
            res.append(c)
            i, j = i + 1, j + 1
        
        return "".join(res) + str1[i:] + str2[j:]
