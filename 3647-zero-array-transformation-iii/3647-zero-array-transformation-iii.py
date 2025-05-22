import heapq
from typing import List

class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        n, m = len(nums), len(queries)
        
        # 1) Feasibility check via difference array
        diff = [0] * (n + 1)
        for l, r in queries:
            diff[l] += 1
            if r + 1 <= n:
                diff[r+1] -= 1
        
        cover = [0] * n
        cur = 0
        for i in range(n):
            cur += diff[i]
            cover[i] = cur
            if cover[i] < nums[i]:
                return -1  # impossible even with all queries
        
        # 2) Greedy multicover on a line
        # Sort queries by left endpoint
        intervals = sorted(queries, key=lambda x: x[0])
        
        available = []   # max‐heap of (–r, r) for queries we can still choose
        active    = []   # min‐heap of r for queries already chosen and still covering i
        used = 0
        idx  = 0
        
        for i in range(n):
            # Add all intervals whose left endpoint == i
            while idx < m and intervals[idx][0] == i:
                r = intervals[idx][1]
                heapq.heappush(available, (-r, r))
                idx += 1
            
            # Drop any chosen intervals that no longer cover i
            while active and active[0] < i:
                heapq.heappop(active)
            
            coverage = len(active)
            need     = nums[i] - coverage
            
            # Greedily pick 'need' intervals that cover i
            for _ in range(need):
                # Remove from available any that can't cover i
                while available and available[0][1] < i:
                    heapq.heappop(available)
                if not available:
                    return -1  # no way to cover position i further
                _, best_r = heapq.heappop(available)
                heapq.heappush(active, best_r)
                used += 1
        
        # We were able to cover every position.  We used `used` queries,
        # so we can remove the rest.
        return m - used
