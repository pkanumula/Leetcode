from collections import Counter
from typing import List

class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        n = len(nums)
        if n == 0:
            return 0

        # Frequency of exact values (no operation needed)
        freq = Counter(nums)

        # Build difference array for coverage of intervals [x-k, x+k]
        mn = min(nums) - k
        mx = max(nums) + k
        size = mx - mn + 3  # +3 to safely index r+1

        diff = [0] * size
        for x in nums:
            l = x - k - mn
            r1 = x + k + 1 - mn
            diff[l] += 1
            diff[r1] -= 1

        ans = 0
        cover = 0
        # Sweep line over all integer targets v
        for i in range(mx - mn + 1):
            cover += diff[i]
            v = i + mn
            f = freq.get(v, 0)
            # Max achievable frequency at v
            cur = min(cover, f + numOperations)
            if cur > ans:
                ans = cur

        return ans
