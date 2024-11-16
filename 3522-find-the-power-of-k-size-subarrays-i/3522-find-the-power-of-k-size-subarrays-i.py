from typing import List

class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        def is_consecutive_and_sorted(subarray: List[int]) -> bool:
            # Check if sorted and consecutive
            for i in range(1, len(subarray)):
                if subarray[i] != subarray[i - 1] + 1:
                    return False
            return True

        results = []
        for i in range(len(nums) - k + 1):
            subarray = nums[i:i + k]
            if is_consecutive_and_sorted(subarray):
                results.append(max(subarray))
            else:
                results.append(-1)
        
        return results