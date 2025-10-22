from typing import List
from bisect import bisect_left, bisect_right

class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        nums.sort()
        n = len(nums)

        # --- 1) maxWindow: largest count inside any interval of length 2k ---
        l = 0
        maxWindow = 0
        for r in range(n):
            while nums[r] - nums[l] > 2 * k:
                l += 1
            maxWindow = max(maxWindow, r - l + 1)

        # --- 2) For each distinct value v, compute W_v and E_v ---
        ans = min(maxWindow, numOperations)  # case x not in nums (E_x = 0)

        i = 0
        while i < n:
            v = nums[i]
            j = i
            while j < n and nums[j] == v:
                j += 1
            E_v = j - i  # occurrences of v
            # Count all elements within [v - k, v + k]
            left = bisect_left(nums, v - k)
            right = bisect_right(nums, v + k)
            W_v = right - left

            cand = min(W_v, E_v + numOperations)
            if cand > ans:
                ans = cand

            i = j

        return ans
