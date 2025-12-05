from typing import List

class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        total = sum(nums)
        n = len(nums)
        
        # If total sum is odd, no valid partitions.
        if total % 2 == 1:
            return 0
        
        # If total sum is even, all n-1 partitions are valid.
        return n - 1
