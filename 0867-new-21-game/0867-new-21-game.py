class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        # Trivial early outs
        if k == 0 or n >= k - 1 + maxPts:
            return 1.0

        dp = [0.0] * (n + 1)
        dp[0] = 1.0

        wsum = 1.0  # sum of dp[i-1]..dp[i-maxPts] for the next i (starts with dp[0])
        res = 0.0

        for i in range(1, n + 1):
            dp[i] = wsum / maxPts
            if i < k:
                # These states can still draw, so they feed the window
                wsum += dp[i]
            else:
                # Terminal states (i >= k) contribute to the answer
                res += dp[i]
            # Maintain window size of at most maxPts
            if i - maxPts >= 0:
                wsum -= dp[i - maxPts]

        return res
