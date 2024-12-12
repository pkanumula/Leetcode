import heapq
from math import sqrt, floor

class Solution:
    def pickGifts(self, gifts: list[int], k: int) -> int:
        # Convert gifts into a max-heap by negating the values
        max_heap = [-gift for gift in gifts]
        heapq.heapify(max_heap)

        for _ in range(k):
            # Extract the largest pile (negate to get the actual value)
            max_gifts = -heapq.heappop(max_heap)
            # Calculate the remaining gifts after taking the square root floor
            remaining_gifts = floor(sqrt(max_gifts))
            # Push the remaining gifts back into the heap (negate for max-heap behavior)
            heapq.heappush(max_heap, -remaining_gifts)

        # Sum up the remaining gifts (convert negatives back to positives)
        return -sum(max_heap)