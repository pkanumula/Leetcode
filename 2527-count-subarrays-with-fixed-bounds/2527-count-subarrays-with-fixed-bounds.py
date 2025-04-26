from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        ans = 0
        min_pos = max_pos = bad_pos = -1
        
        for i, num in enumerate(nums):
            if num < minK or num > maxK:
                bad_pos = i
            if num == minK:
                min_pos = i
            if num == maxK:
                max_pos = i
            ans += max(0, min(min_pos, max_pos) - bad_pos)
        
        return ans
