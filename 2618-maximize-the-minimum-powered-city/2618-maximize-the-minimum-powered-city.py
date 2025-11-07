from typing import List

class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        n = len(stations)

        # Precompute base power of each city via prefix sums
        pref = [0]*(n+1)
        for i, v in enumerate(stations):
            pref[i+1] = pref[i] + v

        def base_power(i: int) -> int:
            L = max(0, i - r)
            R = min(n - 1, i + r)
            return pref[R+1] - pref[L]

        base = [base_power(i) for i in range(n)]
        hi = max(base) + k  # upper bound; safe
        lo = 0

        # Feasibility check: can we reach at least 'target' power everywhere using ≤ k new stations?
        def can(target: int) -> bool:
            extra_diff = [0]*(n+1)     # difference array for added effect over cities
            curr_extra = 0             # running sum of extra effect active at city i
            remaining = k

            for i in range(n):
                curr_extra += extra_diff[i]
                total_here = base[i] + curr_extra
                if total_here < target:
                    need = target - total_here
                    if need > remaining:
                        return False
                    remaining -= need
                    curr_extra += need     # starts affecting from city i
                    end = min(n, i + 2*r + 1)  # effect ends right after this index
                    extra_diff[end] -= need
            return True

        # Binary search the maximum achievable minimum power
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if can(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo
