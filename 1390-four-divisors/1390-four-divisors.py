from typing import List

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        mx = max(nums)

        # Sieve for fast primality checks up to mx
        is_prime = [True] * (mx + 1)
        if mx >= 0: is_prime[0] = False
        if mx >= 1: is_prime[1] = False
        p = 2
        while p * p <= mx:
            if is_prime[p]:
                step = p
                start = p * p
                for x in range(start, mx + 1, step):
                    is_prime[x] = False
            p += 1

        def int_cuberoot(n: int) -> int:
            # floor cube root (safe for n <= 1e5)
            x = int(round(n ** (1.0 / 3.0)))
            while (x + 1) ** 3 <= n:
                x += 1
            while x ** 3 > n:
                x -= 1
            return x

        def sum_if_four(n: int) -> int:
            # Case 1: n = p^3 where p is prime -> divisors: 1, p, p^2, p^3
            r = int_cuberoot(n)
            if r > 1 and r ** 3 == n and is_prime[r]:
                return 1 + r + r * r + n

            # Case 2: n = p*q where p, q are distinct primes -> divisors: 1, p, q, pq
            # Find the smallest divisor > 1 (if any)
            i = 2
            while i * i <= n:
                if n % i == 0:
                    j = n // i
                    if i != j and is_prime[i] and is_prime[j]:
                        return 1 + i + j + n
                    return 0
                i += 1

            return 0

        return sum(sum_if_four(x) for x in nums)
