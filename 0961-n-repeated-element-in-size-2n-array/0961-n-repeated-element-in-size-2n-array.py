from typing import List

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        # The repeated number must match within distance 1, 2, or 3.
        for k in (1, 2, 3):
            for i in range(len(nums) - k):
                if nums[i] == nums[i + k]:
                    return nums[i]
        return -1  # should never happen given constraints
