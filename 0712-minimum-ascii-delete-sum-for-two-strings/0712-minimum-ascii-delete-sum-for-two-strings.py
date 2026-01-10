class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)

        # dp[j] = min delete sum to make s1[:i] and s2[:j] equal (current i row)
        dp = [0] * (n + 1)

        # Base: delete all chars from s2 to match empty s1
        for j in range(1, n + 1):
            dp[j] = dp[j - 1] + ord(s2[j - 1])

        for i in range(1, m + 1):
            ch1 = s1[i - 1]
            prev_diag = dp[0]            # dp[i-1][0]
            dp[0] += ord(ch1)            # dp[i][0] = delete all from s1[:i]

            for j in range(1, n + 1):
                ch2 = s2[j - 1]
                temp = dp[j]             # save dp[i-1][j] before overwriting

                if ch1 == ch2:
                    dp[j] = prev_diag    # keep both chars, no cost
                else:
                    # delete ch1 from s1 OR delete ch2 from s2
                    dp[j] = min(
                        dp[j] + ord(ch1),      # dp[i-1][j] + delete ch1
                        dp[j - 1] + ord(ch2)   # dp[i][j-1] + delete ch2
                    )

                prev_diag = temp          # move diagonal for next j

        return dp[n]
