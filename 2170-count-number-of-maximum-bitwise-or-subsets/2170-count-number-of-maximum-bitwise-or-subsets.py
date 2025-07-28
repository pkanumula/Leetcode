from typing import List

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        n = len(nums)
        # 1) Compute the overall max OR
        target = 0
        for x in nums:
            target |= x

        count = 0
        # 2) Enumerate all non-empty subsets by bitmask
        #    mask runs from 1 to (1<<n)-1
        for mask in range(1, 1 << n):
            curr_or = 0
            # build OR for this subset
            m = mask
            i = 0
            while m:
                if m & 1:
                    curr_or |= nums[i]
                    # early exit: once OR reaches target, no need to keep OR‑ing
                    if curr_or == target:
                        break
                i += 1
                m >>= 1
            # count if we hit the maximum
            if curr_or == target:
                count += 1

        return count
