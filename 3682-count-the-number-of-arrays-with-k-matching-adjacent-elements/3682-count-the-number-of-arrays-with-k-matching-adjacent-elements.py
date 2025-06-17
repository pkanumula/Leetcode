class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        MOD = 10**9 + 7
        
        # Precompute factorials and inverse factorials
        maxN = n
        fact = [1] * (maxN)
        inv_fact = [1] * (maxN)

        for i in range(1, maxN):
            fact[i] = fact[i - 1] * i % MOD

        # Fermat's little theorem for inverse modulo
        inv_fact[maxN - 1] = pow(fact[maxN - 1], MOD - 2, MOD)
        for i in range(maxN - 2, -1, -1):
            inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD

        def comb(a, b):
            if b < 0 or b > a:
                return 0
            return fact[a] * inv_fact[b] % MOD * inv_fact[a - b] % MOD

        res = m * comb(n - 1, k) % MOD * pow(m - 1, n - 1 - k, MOD) % MOD
        return res
