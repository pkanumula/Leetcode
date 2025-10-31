from typing import List

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums) - 2                 # because nums has 0..n-1 plus 2 extra repeats
        seen = [False] * n
        dup = []
        for x in nums:
            if seen[x]:
                dup.append(x)
                if len(dup) == 2:
                    return dup
            else:
                seen[x] = True
        return dup  # safety; constraints guarantee 2 duplicates
