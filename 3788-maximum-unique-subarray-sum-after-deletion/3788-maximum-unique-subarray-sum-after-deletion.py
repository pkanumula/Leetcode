from typing import List

class Solution:
    def maxSum(self, nums: List[int]) -> int:
        # Sum each distinct positive number exactly once
        seen = set()
        total = 0
        for x in nums:
            if x > 0 and x not in seen:
                seen.add(x)
                total += x

        # If we got any positives, total>0 is the answer.
        # Otherwise we have to pick at least one element,
        # so return the maximum (which may be 0 or negative).
        return total if total > 0 else max(nums)
