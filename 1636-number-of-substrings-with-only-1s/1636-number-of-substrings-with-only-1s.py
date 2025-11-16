class Solution:
    def numSub(self, s: str) -> int:
        MOD = 10**9 + 7
        ans = 0
        run = 0  # current consecutive '1's

        for ch in s:
            if ch == '1':
                run += 1
                ans = (ans + run) % MOD  # each '1' extends all-1 substrings ending here
            else:
                run = 0

        return ans % MOD
