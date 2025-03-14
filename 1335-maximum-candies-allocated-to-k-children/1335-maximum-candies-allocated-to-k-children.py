from typing import List

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k:
            return 0
        
        left, right = 1, max(candies)
        
        def can_allocate(mid):
            return sum(c // mid for c in candies) >= k
        
        while left < right:
            mid = (left + right + 1) // 2
            if can_allocate(mid):
                left = mid
            else:
                right = mid - 1
        
        return left
