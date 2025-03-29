from collections import defaultdict
from math import isqrt

MOD = 10**9 + 7

class Solution:
    def maximumScore(self, nums: list[int], k: int) -> int:
        # Function to count distinct prime factors
        def prime_score(x):
            score = 0
            for p in range(2, isqrt(x) + 1):
                if x % p == 0:
                    score += 1
                    while x % p == 0:
                        x //= p
            if x > 1:
                score += 1
            return score

        n = len(nums)
        scores = [prime_score(x) for x in nums]

        # Monotonic stack for next greater prime score
        next_greater = [n] * n
        stack = []
        for i in range(n):
            while stack and scores[stack[-1]] < scores[i]:
                idx = stack.pop()
                next_greater[idx] = i
            stack.append(i)

        # Monotonic stack for previous greater or equal prime score
        prev_greater = [-1] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and scores[stack[-1]] <= scores[i]:
                idx = stack.pop()
                prev_greater[idx] = i
            stack.append(i)

        # Count how many subarrays each element is the max prime score in
        contrib = []
        for i in range(n):
            left = i - prev_greater[i]
            right = next_greater[i] - i
            contrib.append((nums[i], left * right))

        # Sort by value descending to multiply largest numbers first
        contrib.sort(reverse=True)

        res = 1
        for val, cnt in contrib:
            if k == 0:
                break
            take = min(k, cnt)
            res = res * pow(val, take, MOD) % MOD
            k -= take

        return res
