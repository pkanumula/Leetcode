from typing import List
from math import gcd

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Case 1: already have ones
        ones = nums.count(1)
        if ones:
            return n - ones
        
        # Case 2: no ones — check if it's even possible
        g_all = 0
        for x in nums:
            g_all = gcd(g_all, x)
        if g_all != 1:
            return -1
        
        # Case 3: find shortest subarray with gcd == 1
        INF = 10**9
        best = INF
        for i in range(n):
            g = 0
            for j in range(i, n):
                g = gcd(g, nums[j])
                if g == 1:
                    best = min(best, j - i + 1)
                    break  # no need to extend further for this i
        
        # best must be found since overall gcd == 1
        return (best - 1) + (n - 1)
