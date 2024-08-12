import heapq

class KthLargest:

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.min_heap = nums
        heapq.heapify(self.min_heap)  # Create a heap from the list of numbers
        
        # Maintain only the top k elements in the heap
        while len(self.min_heap) > k:
            heapq.heappop(self.min_heap)
        

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        # Add the new value to the heap
        heapq.heappush(self.min_heap, val)
        
        # If the heap exceeds size k, pop the smallest element
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
        
        # The root of the heap is the kth largest element
        return self.min_heap[0]
