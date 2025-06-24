from typing import List

class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        n = len(nums)
        result = set()
        
        # Step 1: Identify all indices where nums[j] == key
        key_indices = [i for i, val in enumerate(nums) if val == key]
        
        # Step 2: For each key index, add all indices within distance k
        for j in key_indices:
            start = max(0, j - k)
            end = min(n - 1, j + k)
            for i in range(start, end + 1):
                result.add(i)
        
        # Step 3: Return the sorted list
        return sorted(result)
