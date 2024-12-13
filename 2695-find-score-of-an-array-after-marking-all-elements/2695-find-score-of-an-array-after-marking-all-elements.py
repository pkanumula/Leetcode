from heapq import heappop, heappush

class Solution:
    def findScore(self, nums):
        n = len(nums)
        marked = [False] * n
        min_heap = []

        # Push all elements into the heap with their indices
        for i, num in enumerate(nums):
            heappush(min_heap, (num, i))

        score = 0

        while min_heap:
            value, idx = heappop(min_heap)
            
            if not marked[idx]:  # Process only if the current element is unmarked
                score += value
                marked[idx] = True

                # Mark adjacent elements if they exist
                if idx > 0:
                    marked[idx - 1] = True
                if idx < n - 1:
                    marked[idx + 1] = True

        return score
