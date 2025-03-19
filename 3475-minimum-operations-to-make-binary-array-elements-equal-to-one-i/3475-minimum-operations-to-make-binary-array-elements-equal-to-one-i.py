from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        operations = 0
        
        for i in range(n - 2):
            if nums[i] == 0:
                # Flip nums[i], nums[i+1], nums[i+2]
                nums[i] ^= 1
                nums[i+1] ^= 1
                nums[i+2] ^= 1
                operations += 1
        
        # If any 0 remains in the last two elements, it's impossible
        return operations if nums[-2] == 1 and nums[-1] == 1 else -1