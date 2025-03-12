from bisect import bisect_left, bisect_right
from typing import List

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        neg_count = bisect_left(nums, 0)  # Find the index of the first non-negative number
        pos_count = len(nums) - bisect_right(nums, 0)  # Find the count of positive numbers
        return max(neg_count, pos_count)
