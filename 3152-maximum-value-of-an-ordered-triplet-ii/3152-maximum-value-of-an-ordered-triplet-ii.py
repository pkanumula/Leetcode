class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        max_val = 0
        max_left = [0] * len(nums)
        max_right = [0] * len(nums)
        
        # Fill max_left, which stores the maximum value from the left side of each element
        max_left[0] = nums[0]
        for i in range(1, len(nums)):
            max_left[i] = max(max_left[i - 1], nums[i])
        
        # Fill max_right, which stores the maximum value from the right side of each element
        max_right[len(nums) - 1] = nums[len(nums) - 1]
        for i in range(len(nums) - 2, -1, -1):
            max_right[i] = max(max_right[i + 1], nums[i])
        
        # Calculate the triplet value
        for j in range(1, len(nums) - 1):
            left_value = max_left[j - 1] - nums[j]
            right_value = max_right[j + 1]
            max_val = max(max_val, left_value * right_value)
        
        return max_val
