from typing import List

class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        next_free = -10**30  # the smallest integer we haven't used yet
        ans = 0

        for x in nums:
            # The earliest we can place this number is x-k,
            # but we cannot go earlier than next_free.
            place = max(next_free, x - k)

            # If that placement is still within [x-k, x+k], we can use it.
            if place <= x + k:
                ans += 1
                next_free = place + 1  # move the "used" boundary forward

        return ans
