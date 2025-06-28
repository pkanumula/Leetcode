from typing import List

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        # Pair each number with its index
        indexed_nums = list(enumerate(nums))
        
        # Sort by value descending, but keep index for order recovery
        top_k = sorted(indexed_nums, key=lambda x: x[1], reverse=True)[:k]
        
        # Sort the selected k elements by original index to maintain subsequence order
        top_k_sorted = sorted(top_k, key=lambda x: x[0])
        
        # Extract the values and return
        return [num for idx, num in top_k_sorted]
