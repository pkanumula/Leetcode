class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        zero_count = 0
        max_len = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1
            
            # If more than one zero, shrink the window
            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            
            # Length of window minus 1 (because we must delete one element)
            max_len = max(max_len, right - left)
        
        return max_len
