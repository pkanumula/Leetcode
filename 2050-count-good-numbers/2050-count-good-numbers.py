class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
        
        def power(x, y):
            result = 1
            x = x % MOD
            while y > 0:
                if y % 2 == 1:
                    result = (result * x) % MOD
                x = (x * x) % MOD
                y //= 2
            return result

        even_count = (n + 1) // 2  # digits at even indices
        odd_count = n // 2         # digits at odd indices

        return (power(5, even_count) * power(4, odd_count)) % MOD
