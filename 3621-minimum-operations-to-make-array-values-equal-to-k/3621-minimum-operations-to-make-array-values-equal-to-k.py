class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # Check if there is any number that is below k.
        if any(num < k for num in nums):
            return -1
        
        # Count the distinct numbers that are greater than k.
        return len({num for num in nums if num > k})
