from typing import List

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        # Count how many evens (0) and odds (1) we have
        cnt = [0, 0]
        parity = [x & 1 for x in nums]
        for p in parity:
            cnt[p] += 1

        # Case 1: pick all of one parity
        best_constant = max(cnt)  

        # Case 2: longest alternating subsequence
        def alt_len(start_parity: int) -> int:
            needed = start_parity
            length = 0
            for p in parity:
                if p == needed:
                    length += 1
                    needed ^= 1
            return length

        best_alternating = max(alt_len(0), alt_len(1))

        return max(best_constant, best_alternating)
