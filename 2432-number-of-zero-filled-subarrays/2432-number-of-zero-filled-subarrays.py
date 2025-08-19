from typing import List

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        count = 0   # streak of consecutive zeros
        result = 0  # total subarrays
        for num in nums:
            if num == 0:
                count += 1
                result += count  # each new zero adds `count` subarrays
            else:
                count = 0
        return result
