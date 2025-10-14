from typing import List

class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        # inc_len[i] = length of strictly increasing run ending at i
        inc_len = [1] * n
        for i in range(1, n):
            if nums[i-1] < nums[i]:
                inc_len[i] = inc_len[i-1] + 1

        # valid_start[s] = subarray nums[s:s+k] is strictly increasing
        valid_start = [False] * (n - k + 1)
        for s in range(0, n - k + 1):
            if inc_len[s + k - 1] >= k:
                valid_start[s] = True

        # Need two adjacent windows: starts at s and s+k
        # s can go up to n - 2k
        for s in range(0, n - 2 * k + 1):
            if valid_start[s] and valid_start[s + k]:
                return True

        return False
