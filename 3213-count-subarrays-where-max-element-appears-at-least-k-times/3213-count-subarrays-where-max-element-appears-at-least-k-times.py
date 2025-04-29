from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_num = max(nums)
        count = 0
        left = 0
        ans = 0
        
        for right in range(len(nums)):
            if nums[right] == max_num:
                count += 1
            while count >= k:
                if nums[left] == max_num:
                    count -= 1
                left += 1
            ans += left
        return ans
