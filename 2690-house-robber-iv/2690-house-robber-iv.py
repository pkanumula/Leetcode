from typing import List

class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def can_rob_with_capability(cap: int) -> bool:
            count, i = 0, 0
            while i < len(nums):
                if nums[i] <= cap:
                    count += 1
                    i += 1  # Skip the next adjacent house
                i += 1
                if count >= k:
                    return True
            return False
        
        left, right = min(nums), max(nums)
        while left < right:
            mid = (left + right) // 2
            if can_rob_with_capability(mid):
                right = mid
            else:
                left = mid + 1
        return left
