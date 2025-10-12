from typing import List

class Solution:
    def magicalSum(self, m: int, k: int, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        # nCk up to m
        comb = [[0]*(m+1) for _ in range(m+1)]
        for i in range(m+1):
            comb[i][0] = 1
            for j in range(1, i+1):
                comb[i][j] = (comb[i-1][j-1] + comb[i-1][j]) % MOD

        # powers nums[j]^c for c = 0..m
        powv = [[1]*(m+1) for _ in range(n)]
        for j in range(n):
            for c in range(1, m+1):
                powv[j][c] = (powv[j][c-1] * nums[j]) % MOD

        # dp[t][carry] is a vector of length (k+1): counts for s set bits so far
        dp = [ [ [0]*(k+1) for _ in range(m+1) ] for __ in range(m+1) ]
        dp[0][0][0] = 1

        for j in range(n):
            newdp = [ [ [0]*(k+1) for _ in range(m+1) ] for __ in range(m+1) ]
            for t in range(m+1):
                rem = m - t
                for carry in range(m+1):
                    vec = dp[t][carry]
                    if not any(vec):
                        continue
                    for c in range(rem+1):
                        ones_bit = (carry + c) & 1
                        carry2   = (carry + c) >> 1
                        t2 = t + c
                        weight = (comb[rem][c] * powv[j][c]) % MOD
                        dest = newdp[t2][carry2]
                        if ones_bit == 0:
                            for s in range(k+1):
                                if vec[s]:
                                    dest[s] = (dest[s] + vec[s]*weight) % MOD
                        else:
                            for s in range(k):
                                if vec[s]:
                                    dest[s+1] = (dest[s+1] + vec[s]*weight) % MOD
            dp = newdp

        def popcount(x: int) -> int:
            return bin(x).count("1")

        ans = 0
        # After last position, remaining carry contributes popcount(carry) to set bits
        for carry in range(m+1):
            pc = popcount(carry)
            if pc <= k:
                ans = (ans + dp[m][carry][k - pc]) % MOD

        return ans
