import heapq

class Solution(object):
    def maxKelements(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Create a max-heap using negative numbers
        max_heap = [-num for num in nums]
        heapq.heapify(max_heap)
        
        score = 0
        
        # Perform k operations
        for _ in range(k):
            # Extract the largest element (negate it back to positive)
            largest = -heapq.heappop(max_heap)
            
            # Increase the score
            score += largest
            
            # Replace the element with ceil(largest / 3) and push it back into the heap
            new_val = (largest + 2) // 3  # Equivalent to ceil(largest / 3)
            heapq.heappush(max_heap, -new_val)
        
        return score
