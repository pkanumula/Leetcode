from typing import List
from collections import defaultdict

MOD = 10**9 + 7

class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        right = defaultdict(int)
        for x in nums:
            right[x] += 1

        left = defaultdict(int)
        ans = 0

        for j, x in enumerate(nums):
            # current index leaves the right side
            right[x] -= 1

            v = 2 * x
            # count pairs (i, k) around j
            ans = (ans + left.get(v, 0) * right.get(v, 0)) % MOD

            # current index enters the left side
            left[x] += 1

        return ans
