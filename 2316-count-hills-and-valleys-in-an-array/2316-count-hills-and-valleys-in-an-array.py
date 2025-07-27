from typing import List

class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        prev_state = None  # 'hill', 'valley', or None
        
        for i in range(1, n - 1):
            # Find closest non-equal neighbor on left
            left = i - 1
            while left >= 0 and nums[left] == nums[i]:
                left -= 1
            
            # Find closest non-equal neighbor on right
            right = i + 1
            while right < n and nums[right] == nums[i]:
                right += 1
            
            # If no non-equal neighbor on either side, continue
            if left < 0 or right >= n:
                continue
            
            if nums[i] > nums[left] and nums[i] > nums[right]:
                # Hill
                if prev_state != 'hill':
                    count += 1
                    prev_state = 'hill'
            elif nums[i] < nums[left] and nums[i] < nums[right]:
                # Valley
                if prev_state != 'valley':
                    count += 1
                    prev_state = 'valley'
            else:
                # Neither hill nor valley
                prev_state = None
                
        return count
