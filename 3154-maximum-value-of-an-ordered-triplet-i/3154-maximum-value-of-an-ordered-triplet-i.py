class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        max_val = 0
        left_max = [0] * n
        right_max = [0] * n
        
        # Calculate the maximum value from the left side for each element
        left_max[0] = nums[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], nums[i])
        
        # Calculate the maximum value from the right side for each element
        right_max[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], nums[i])
        
        # Now, check for each valid triplet (i, j, k)
        for j in range(1, n - 1):
            left = left_max[j - 1]
            right = right_max[j + 1]
            val = (left - nums[j]) * right
            if val > max_val:
                max_val = val
        
        return max_val if max_val > 0 else 0
