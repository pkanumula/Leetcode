from typing import List

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        # Generate a list of primes using the Sieve of Eratosthenes
        sieve = [True] * (right + 1)
        sieve[0] = sieve[1] = False
        p = 2
        while p * p <= right:
            if sieve[p]:
                for i in range(p * p, right + 1, p):
                    sieve[i] = False
            p += 1

        # Collect primes within the range [left, right]
        primes = [i for i in range(max(2, left), right + 1) if sieve[i]]

        # Find the pair with the smallest difference
        if len(primes) < 2:
            return [-1, -1]

        min_diff = float('inf')
        result = [-1, -1]
        for i in range(len(primes) - 1):
            diff = primes[i + 1] - primes[i]
            if diff < min_diff:
                min_diff = diff
                result = [primes[i], primes[i + 1]]

        return result