from math import log, ceil

class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        def prefix(n: int) -> int:
            if n <= 0:
                return 0
            total = 0
            k = 0
            base = 1
            while base * 4 <= n:
                total += (base * 3) * (k+1)   # full block contribution
                k += 1
                base *= 4
            total += (n - base + 1) * (k+1)  # partial block
            return total

        ans = 0
        for l, r in queries:
            s = prefix(r) - prefix(l-1)
            ans += (s + 1)//2   # ceil(s/2)
        return ans
