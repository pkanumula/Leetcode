class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Step 1: Find the maximum element in the array
        max_num = max(nums)
        
        # Step 2: Traverse through the array to find the longest subarray of max_num
        longest = 0
        current_length = 0
        
        for num in nums:
            if num == max_num:
                # If the current number is equal to the maximum, extend the current subarray
                current_length += 1
                longest = max(longest, current_length)
            else:
                # If not, reset the current subarray length
                current_length = 0
        
        return longest
