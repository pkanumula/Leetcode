from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # 1. Find the max value k
        k = max(nums)
        # 2. Scan and count longest run of k’s
        max_len = curr = 0
        for x in nums:
            if x == k:
                curr += 1
                max_len = max(max_len, curr)
            else:
                curr = 0
        return max_len
