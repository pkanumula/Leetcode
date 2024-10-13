import heapq

class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        # Min-heap to store the smallest element from each list
        min_heap = []
        
        # Initialize the range
        current_max = float('-inf')
        for i in range(len(nums)):
            heapq.heappush(min_heap, (nums[i][0], i, 0))
            current_max = max(current_max, nums[i][0])

        # Start with an initial range that is very large
        result = [float('-inf'), float('inf')]
        
        # Iterate through the min-heap to find the smallest range
        while min_heap:
            current_min, row, idx = heapq.heappop(min_heap)
            
            # Check if the current range is smaller than the previous best range
            if current_max - current_min < result[1] - result[0]:
                result = [current_min, current_max]
            
            # Move to the next element in the current row
            if idx + 1 == len(nums[row]):
                break  # If one of the lists is exhausted, we are done
            next_val = nums[row][idx + 1]
            heapq.heappush(min_heap, (next_val, row, idx + 1))
            current_max = max(current_max, next_val)
        
        return result
