class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10**9 + 7
        
        # dp[i][j][k]: # stable arrays with i zeros, j ones, ending in k
        dp = [[[0, 0] for _ in range(one + 1)] for _ in range(zero + 1)]
        
        # Base cases: arrays of only 0s or only 1s (length <= limit)
        for i in range(1, min(zero, limit) + 1):
            dp[i][0][0] = 1
        for j in range(1, min(one, limit) + 1):
            dp[0][j][1] = 1
        
        for i in range(1, zero + 1):
            for j in range(1, one + 1):
                # Ending in 0: came from ending in 0 or 1, then placed a 0
                dp[i][j][0] = (dp[i-1][j][0] + dp[i-1][j][1]) % MOD
                # Subtract: would create run of limit+1 zeros
                # That means limit zeros before this, preceded by a 1
                if i >= limit + 1:
                    dp[i][j][0] = (dp[i][j][0] - dp[i-limit-1][j][1]) % MOD
                # Edge: pure block of (limit+1) zeros at start, j ones after... 
                # handled since dp[i-limit-1][0][1] = 0 for i-limit-1 >= 1
                
                # Ending in 1: came from ending in 0 or 1, then placed a 1
                dp[i][j][1] = (dp[i][j-1][0] + dp[i][j-1][1]) % MOD
                # Subtract: would create run of limit+1 ones
                if j >= limit + 1:
                    dp[i][j][1] = (dp[i][j][1] - dp[i][j-limit-1][0]) % MOD
        
        return (dp[zero][one][0] + dp[zero][one][1]) % MOD