class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10**9 + 7

        aba = 6  # patterns like A B A
        abc = 6  # patterns like A B C

        for _ in range(1, n):
            prev_aba, prev_abc = aba, abc
            aba = (3 * prev_aba + 2 * prev_abc) % MOD
            abc = (2 * prev_aba + 2 * prev_abc) % MOD

        return (aba + abc) % MOD
