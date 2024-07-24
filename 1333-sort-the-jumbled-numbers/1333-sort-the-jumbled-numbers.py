class Solution(object):
    def sortJumbled(self, mapping, nums):
        """
        :type mapping: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        def get_mapped_value(num):
            if num == 0:
                return mapping[0]
            
            mapped = 0
            multiplier = 1
            while num:
                digit = num % 10
                mapped += mapping[digit] * multiplier
                multiplier *= 10
                num //= 10
            return mapped

        # Create a list of tuples: (original index, original number, mapped value)
        indexed_nums = [(i, num, get_mapped_value(num)) for i, num in enumerate(nums)]
        
        # Sort the list based on mapped value and original index
        indexed_nums.sort(key=lambda x: (x[2], x[0]))
        
        # Extract the sorted original numbers
        return [num for _, num, _ in indexed_nums]