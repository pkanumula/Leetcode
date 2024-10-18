class Solution(object):
    def countMaxOrSubsets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Calculate the maximum possible bitwise OR for the array
        max_or = 0
        for num in nums:
            max_or |= num
        
        # Use backtracking to count subsets that achieve the maximum OR
        def backtrack(index, current_or):
            # If we have reached the end of the array
            if index == len(nums):
                # If the current OR matches the maximum OR, it's a valid subset
                return 1 if current_or == max_or else 0
            
            # Two choices: include nums[index] or exclude it
            include_count = backtrack(index + 1, current_or | nums[index])
            exclude_count = backtrack(index + 1, current_or)
            
            # Return the sum of counts from both choices
            return include_count + exclude_count
        
        # Start backtracking from the first index with an initial OR of 0
        return backtrack(0, 0)