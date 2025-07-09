from typing import List

class Solution:
    def maxFreeTime(self, eventTime: int,
                    k: int,
                    startTime: List[int],
                    endTime:   List[int]) -> int:
        n = len(startTime)

        # 1. build the gaps array
        gaps = [startTime[0]]                          # before first meeting
        for i in range(1, n):
            gaps.append(startTime[i] - endTime[i-1])   # between meetings
        gaps.append(eventTime - endTime[-1])           # after last meeting

        # 2. largest window we are allowed to merge
        w = min(k + 1, n + 1)

        # 3. sliding-window maximum of size w
        cur = sum(gaps[:w])
        best = cur
        for i in range(w, n + 1):          # gaps has length n+1
            cur += gaps[i] - gaps[i - w]
            if cur > best:
                best = cur
        return best
