class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        
        # Collect exponents (bit positions) for set bits in n, in ascending order
        exps = []
        bit = 0
        while (1 << bit) <= n:
            if (n >> bit) & 1:
                exps.append(bit)
            bit += 1
        
        # Prefix sums of exponents
        pref = [0]
        for e in exps:
            pref.append(pref[-1] + e)
        
        # Answer queries: product is 2^(sum of exponents in range)
        ans = []
        for l, r in queries:
            total_exp = pref[r + 1] - pref[l]
            ans.append(pow(2, total_exp, MOD))
        return ans
