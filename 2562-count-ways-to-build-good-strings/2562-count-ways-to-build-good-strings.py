class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 10**9 + 7

        # dp[i] will store the number of good strings of length i
        dp = [0] * (high + 1)
        dp[0] = 1  # Base case: empty string

        for length in range(1, high + 1):
            if length >= zero:
                dp[length] += dp[length - zero]  # Add strings ending with '0'
            if length >= one:
                dp[length] += dp[length - one]  # Add strings ending with '1'
            dp[length] %= MOD

        # Sum up the counts for lengths between low and high (inclusive)
        result = sum(dp[low:high + 1]) % MOD
        return result
