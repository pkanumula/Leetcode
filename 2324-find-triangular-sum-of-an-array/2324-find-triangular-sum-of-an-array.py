from typing import List

class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        # Keep reducing the list until only one element is left
        while len(nums) > 1:
            newNums = []
            for i in range(len(nums) - 1):
                newNums.append((nums[i] + nums[i + 1]) % 10)
            nums = newNums
        return nums[0]
