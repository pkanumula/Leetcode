from typing import List
import bisect

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        ans = [-1] * n
        last = {}            # lake -> last rainy day index
        dry_days = []        # sorted indices of days with rains[i] == 0

        for i, lake in enumerate(rains):
            if lake == 0:
                # tentatively put 1; we'll overwrite if we need this day to dry a specific lake
                ans[i] = 1
                bisect.insort(dry_days, i)
            else:
                # it's raining on 'lake'
                if lake in last:
                    # need a dry day after last[lake]
                    j = last[lake]
                    idx = bisect.bisect_right(dry_days, j)
                    if idx == len(dry_days):
                        return []   # no dry day available after last rain -> flood
                    k = dry_days.pop(idx)   # use the earliest valid dry day
                    ans[k] = lake           # dry this lake on day k
                # mark today as the last rain day for this lake
                last[lake] = i
                ans[i] = -1                 # raining days must be -1 per spec

        return ans
