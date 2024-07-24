class Solution:
    def sortJumbled(self, mapping, nums):
        def get_mapped_value(num):
            if num == 0:
                return mapping[0]
            
            mapped = 0
            power = 1
            while num > 0:
                digit = num % 10
                mapped += mapping[digit] * power
                num //= 10
                power *= 10
            return mapped

        # Create a list of tuples: (original index, original number, mapped value)
        indexed_nums = [(i, num, get_mapped_value(num)) for i, num in enumerate(nums)]
        
        # Sort the list based on mapped value and original index
        indexed_nums.sort(key=lambda x: (x[2], x[0]))
        
        # Extract the original numbers in the new order
        return [num for _, num, _ in indexed_nums]