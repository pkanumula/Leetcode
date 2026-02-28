class Solution:
    def concatenatedBinary(self, n: int) -> int:
        MOD = 10**9 + 7
        ans = 0
        bits = 0  # current bit-length to shift by

        for i in range(1, n + 1):
            # bit-length increases exactly at powers of 2: 1,2,4,8,...
            if i & (i - 1) == 0:
                bits += 1

            ans = ((ans << bits) + i) % MOD

        return ans