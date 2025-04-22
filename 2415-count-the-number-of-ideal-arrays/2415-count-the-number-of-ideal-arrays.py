from math import comb
from functools import lru_cache

MOD = 10**9 + 7

class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        @lru_cache(None)
        def count_combinations(length, freq):
            return comb(n - 1, freq - 1)

        # Precompute divisors up to maxValue
        divisors = [[] for _ in range(maxValue + 1)]
        for i in range(1, maxValue + 1):
            for j in range(i * 2, maxValue + 1, i):
                divisors[j].append(i)

        dp = [0] * (maxValue + 1)
        for i in range(1, maxValue + 1):
            dp[i] = 1  # Base case: length 1

        res = 0
        max_len = 14  # Since 2^14 > 10000, max possible length of sequence

        # ways[val][length] = number of ideal arrays ending with val and of that length
        ways = [[0] * (max_len + 1) for _ in range(maxValue + 1)]

        for i in range(1, maxValue + 1):
            ways[i][1] = 1

        for length in range(2, max_len + 1):
            for val in range(1, maxValue + 1):
                for d in divisors[val]:
                    ways[val][length] = (ways[val][length] + ways[d][length - 1]) % MOD

        for val in range(1, maxValue + 1):
            for length in range(1, max_len + 1):
                if ways[val][length]:
                    res = (res + ways[val][length] * comb(n - 1, length - 1)) % MOD

        return res
