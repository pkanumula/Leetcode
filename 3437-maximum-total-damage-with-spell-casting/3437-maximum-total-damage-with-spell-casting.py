from typing import List
from collections import Counter
import bisect

class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        # Count occurrences, each value contributes value * count if chosen
        cnt = Counter(power)
        vals = sorted(cnt)                            # unique damages
        weights = [v * cnt[v] for v in vals]          # total gain if we pick damage v

        n = len(vals)
        if n == 0:
            return 0

        dp = [0] * n  # dp[i] = best total using vals[0..i]

        for i, x in enumerate(vals):
            # find the rightmost index j < i with vals[j] <= x - 3 (non-conflicting)
            j = bisect.bisect_right(vals, x - 3, 0, i) - 1
            take = weights[i] + (dp[j] if j >= 0 else 0)
            skip = dp[i - 1] if i > 0 else 0
            dp[i] = max(skip, take)

        return dp[-1]
