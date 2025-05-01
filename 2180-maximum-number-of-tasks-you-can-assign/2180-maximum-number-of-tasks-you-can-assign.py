from collections import deque
import bisect

class Solution:
    def maxTaskAssign(self, tasks, workers, pills, strength):
        tasks.sort()
        workers.sort()

        def can_assign(k):
            task_q = deque(tasks[:k])
            available = workers[-k:]
            pill_left = pills
            i = k - 1  # strongest remaining worker index
            for t in reversed(tasks[:k]):
                # Assign strongest available worker
                if available[i] >= t:
                    i -= 1
                    continue
                # Try to use pill on weakest possible worker
                idx = bisect.bisect_left(available, t - strength, 0, i + 1)
                if idx > i or pill_left == 0:
                    return False
                del available[idx]
                i -= 1
                pill_left -= 1
            return True

        l, r, ans = 0, min(len(tasks), len(workers)), 0
        while l <= r:
            mid = (l + r) // 2
            if can_assign(mid):
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans
