from typing import List

class Solution:
    def maxFreeTime(self,
                    eventTime: int,
                    startTime:  List[int],
                    endTime:    List[int]) -> int:
        n = len(startTime)
        # 1. Build the gaps array: gaps[i] is free time before meeting i (so gaps[0] is before the 1st,
        #    gaps[n] is after the last)
        gaps = [0] * (n + 1)
        gaps[0] = startTime[0]
        for i in range(1, n):
            gaps[i] = startTime[i] - endTime[i-1]
        gaps[n] = eventTime - endTime[-1]

        # 2. Original maximum free gap
        G0 = max(gaps)

        # 3. Prefix‐/suffix‐max to get, for each i,
        #    SM = max(gaps excluding gaps[i], gaps[i+1])
        prefix_max = [0] * (n + 2)
        for i in range(1, n+2):
            prefix_max[i] = max(prefix_max[i-1], gaps[i-1])
        suffix_max = [0] * (n + 2)
        for i in range(n, -1, -1):
            suffix_max[i] = max(suffix_max[i+1], gaps[i])

        best_overall = G0

        # 4. Try moving each meeting i
        for i in range(n):
            d = endTime[i] - startTime[i]
            # merged gap after removal
            M = gaps[i] + d + gaps[i+1]

            if M <= G0:
                # Can't beat the original
                candidate = G0
            else:
                # largest other gap after removing gaps[i], gaps[i+1]
                SM = max(prefix_max[i], suffix_max[i+2])
                if SM >= d:
                    # can split some other gap ≥ d, leaving M intact
                    candidate = M
                else:
                    # must split M itself
                    candidate = max(SM, M - d)

            best_overall = max(best_overall, candidate)

        return best_overall
