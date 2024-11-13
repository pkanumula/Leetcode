from typing import List

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        n = len(nums)
        count = 0
        
        def count_pairs_with_sum_at_most(limit: int) -> int:
            left, right = 0, n - 1
            total = 0
            while left < right:
                if nums[left] + nums[right] <= limit:
                    total += right - left
                    left += 1
                else:
                    right -= 1
            return total
        
        return count_pairs_with_sum_at_most(upper) - count_pairs_with_sum_at_most(lower - 1)
