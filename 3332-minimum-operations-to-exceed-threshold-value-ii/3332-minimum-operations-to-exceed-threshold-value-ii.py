import heapq
from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)  # Convert nums into a min-heap
        operations = 0

        while nums[0] < k:  # Keep processing until the smallest element is >= k
            x = heapq.heappop(nums)  # Extract the smallest element
            y = heapq.heappop(nums)  # Extract the second smallest element
            new_element = min(x, y) * 2 + max(x, y)  # Compute the new element
            heapq.heappush(nums, new_element)  # Push new element back into heap
            operations += 1  # Increment operation count

        return operations
