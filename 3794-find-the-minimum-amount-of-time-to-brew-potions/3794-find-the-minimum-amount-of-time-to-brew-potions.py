from typing import List

class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        n, m = len(skill), len(mana)
        # prefix sums of skills
        SA = [0]*n
        run = 0
        for i, a in enumerate(skill):
            run += a
            SA[i] = run

        # accumulate start-time differences (lags) between consecutive potions
        total_lag = 0
        for j in range(m - 1):
            Bj, Bj1 = mana[j], mana[j + 1]
            # L_j = max_i (Bj*SA[i] - Bj1*SA[i-1]), where SA[-1] := 0
            mx = float('-inf')
            for i in range(n):
                SAi = SA[i]
                SAim1 = SA[i - 1] if i > 0 else 0
                val = Bj * SAi - Bj1 * SAim1
                if val > mx:
                    mx = val
            total_lag += mx  # note: mx >= p_{0,j} = Bj*skill[0] ≥ 0

        # final completion = start of last potion + time it spends on all wizards
        return total_lag + mana[-1] * SA[-1]
