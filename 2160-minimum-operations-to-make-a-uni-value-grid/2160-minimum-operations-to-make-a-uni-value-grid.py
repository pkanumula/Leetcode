class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        nums = [num for row in grid for num in row]
        base = nums[0]
        
        # Check if transformation is possible
        for num in nums:
            if (num - base) % x != 0:
                return -1
        
        # Convert all numbers to their x-multiples relative to base
        nums = [(num - base) // x for num in nums]
        nums.sort()
        median = nums[len(nums) // 2]
        
        # Calculate total operations to reach median
        return sum(abs(num - median) for num in nums)
