import heapq
from typing import List

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        m = len(nums)
        N = m // 3

        # 1) Prefix sums (smallest N in prefix)
        pre = [0] * (m + 1)
        max_heap = []
        s = 0
        for i in range(2*N):
            heapq.heappush(max_heap, -nums[i])
            s += nums[i]
            if len(max_heap) > N:
                s += heapq.heappop(max_heap)  # remove one smallest by popping largest negative
            if i+1 >= N:
                pre[i+1] = s

        # 2) Suffix sums (largest N in suffix)
        suf = [0] * (m + 1)
        min_heap = []
        s = 0
        for i in range(m-1, N-1, -1):
            heapq.heappush(min_heap, nums[i])
            s += nums[i]
            if len(min_heap) > N:
                s -= heapq.heappop(min_heap)
            suf[i] = s

        # 3) Compute answer
        ans = float('inf')
        for i in range(N, 2*N+1):
            ans = min(ans, pre[i] - suf[i])
        return ans
