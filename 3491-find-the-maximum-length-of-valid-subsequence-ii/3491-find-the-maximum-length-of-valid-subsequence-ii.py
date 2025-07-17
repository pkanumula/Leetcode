from typing import List

class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # Precompute residues
        rem = [x % k for x in nums]

        ans = 1  # at least one element is always a valid subsequence
        # Try every target remainder R
        for R in range(k):
            # best[c] = best dp-value so far ending with residue c
            best = [-10**9] * k
            dpj = 1
            best[rem[0]] = 1

            # initialize with j=0
            curr_max = 1

            for j in range(1, n):
                need = (R - rem[j]) % k
                if best[need] > 0:
                    dpj = best[need] + 1
                else:
                    dpj = 1
                # update
                if dpj > best[rem[j]]:
                    best[rem[j]] = dpj
                if dpj > curr_max:
                    curr_max = dpj

            if curr_max > ans:
                ans = curr_max

        return ans
