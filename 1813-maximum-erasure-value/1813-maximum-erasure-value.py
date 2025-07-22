from typing import List

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        l = 0
        cur_sum = 0
        max_sum = 0
        seen = set()
        
        for r, x in enumerate(nums):
            # If duplicate, shrink from left until it's gone
            while x in seen:
                seen.remove(nums[l])
                cur_sum -= nums[l]
                l += 1
            
            # Add the new unique element
            seen.add(x)
            cur_sum += x
            
            # Update answer
            if cur_sum > max_sum:
                max_sum = cur_sum
        
        return max_sum
