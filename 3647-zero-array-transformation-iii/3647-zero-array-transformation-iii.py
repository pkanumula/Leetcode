import heapq
from typing import List

class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        n, m = len(nums), len(queries)
        # 1) Feasibility via difference array
        diff = [0] * (n + 1)
        for l, r in queries:
            diff[l] += 1
            diff[r + 1] -= 1

        cover = 0
        for i, need in enumerate(nums):
            cover += diff[i]
            if cover < need:
                return -1  # even using all queries we can't meet nums[i]

        # 2) Greedy scan with two heaps
        intervals = sorted(queries)        # sort by l ascending
        avail, active = [], []             # avail: max-heap of r; active: min-heap of r
        used = j = 0

        for i in range(n):
            # push all intervals starting at i into avail
            while j < m and intervals[j][0] == i:
                heapq.heappush(avail, -intervals[j][1])
                j += 1

            # drop expired active intervals
            while active and active[0] < i:
                heapq.heappop(active)

            # cover deficit at i
            deficit = nums[i] - len(active)
            for _ in range(deficit):
                # prune unusable intervals
                while avail and -avail[0] < i:
                    heapq.heappop(avail)
                if not avail:
                    return -1
                r = -heapq.heappop(avail)
                heapq.heappush(active, r)
                used += 1

        return m - used
