class Solution(object):
    def minSwaps(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        total_ones = sum(nums)
        
        if total_ones == 0:
            return 0
        
        # Initial window size
        window_size = total_ones
        
        # Find the number of 1s in the initial window
        current_ones = sum(nums[:window_size])
        
        # Start with the number of swaps needed for the initial window
        min_swaps = window_size - current_ones
        
        # Sliding window across the array
        for i in range(1, n):
            # Remove the element that's sliding out of the window
            if nums[i - 1] == 1:
                current_ones -= 1
            
            # Add the element that's sliding into the window
            if nums[(i + window_size - 1) % n] == 1:
                current_ones += 1
            
            # Calculate swaps needed for the current window
            current_swaps = window_size - current_ones
            min_swaps = min(min_swaps, current_swaps)
        
        return min_swaps
