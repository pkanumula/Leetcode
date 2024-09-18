from functools import cmp_to_key

class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        # Convert all integers in the list to strings
        nums = list(map(str, nums))
        
        # Custom comparator function to decide order based on string concatenation
        def compare(x, y):
            if x + y > y + x:
                return -1  # x should come before y
            else:
                return 1  # y should come before x
        
        # Sort the array using the custom comparator
        nums.sort(key=cmp_to_key(compare))
        
        # Special case: if the largest number is '0', return '0' (e.g., [0, 0])
        if nums[0] == '0':
            return '0'
        
        # Join the sorted array into a single string and return
        return ''.join(nums)
