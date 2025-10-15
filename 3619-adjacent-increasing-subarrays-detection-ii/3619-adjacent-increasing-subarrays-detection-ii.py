from typing import List

class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0  # can't have two adjacent subarrays

        # L[i]: length of increasing run ending at i
        L = [1] * n
        for i in range(1, n):
            if nums[i-1] < nums[i]:
                L[i] = L[i-1] + 1

        # R[i]: length of increasing run starting at i
        R = [1] * n
        for i in range(n-2, -1, -1):
            if nums[i] < nums[i+1]:
                R[i] = R[i+1] + 1

        ans = 0
        # split between b-1 and b; both sides must exist
        for b in range(1, n):
            ans = max(ans, min(L[b-1], R[b]))

        return ans
