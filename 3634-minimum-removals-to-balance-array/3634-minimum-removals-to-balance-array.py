from typing import List

class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)

        max_keep = 1
        r = 0

        # Sliding window on sorted array:
        # for each left index l, expand r while nums[r] <= nums[l] * k
        for l in range(n):
            while r < n and nums[r] <= nums[l] * k:
                r += 1
            # window [l, r-1] is valid
            max_keep = max(max_keep, r - l)

            # keep r at least l+1 for next iteration (optional safety)
            if r == l:
                r += 1

        return n - max_keep
