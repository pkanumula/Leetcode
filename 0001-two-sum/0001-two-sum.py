class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Create a dictionary to store the index of each number we have seen
        num_to_index = {}
        
        # Iterate over the list with index
        for i, num in enumerate(nums):
            # Calculate the complement
            complement = target - num
            
            # Check if the complement is already in the dictionary
            if complement in num_to_index:
                # Return the indices of the complement and the current number
                return [num_to_index[complement], i]
            
            # Store the index of the current number in the dictionary
            num_to_index[num] = i
        
        # If no solution found (this line should never be reached given the problem constraints)
        return []