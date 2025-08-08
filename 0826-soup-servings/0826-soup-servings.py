class Solution:
    def soupServings(self, n: int) -> float:
        from functools import lru_cache
        import math
        
        # Optimization: for large n, answer ~ 1.0
        if n > 4800:
            return 1.0
        
        # Scale down
        n = math.ceil(n / 25)
        
        @lru_cache(None)
        def dp(a, b):
            if a <= 0 and b <= 0:
                return 0.5
            if a <= 0:
                return 1.0
            if b <= 0:
                return 0.0
            return 0.25 * (
                dp(a - 4, b) +
                dp(a - 3, b - 1) +
                dp(a - 2, b - 2) +
                dp(a - 1, b - 3)
            )
        
        return dp(n, n)
