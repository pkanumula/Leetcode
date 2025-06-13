from typing import List

class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        
        def can_form_pairs(max_diff: int) -> bool:
            count = 0
            i = 0
            while i < len(nums) - 1:
                if nums[i+1] - nums[i] <= max_diff:
                    count += 1
                    i += 2  # skip the next one (both are used)
                else:
                    i += 1  # try next pair
            return count >= p
        
        low, high = 0, nums[-1] - nums[0]
        answer = high
        
        while low <= high:
            mid = (low + high) // 2
            if can_form_pairs(mid):
                answer = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return answer
