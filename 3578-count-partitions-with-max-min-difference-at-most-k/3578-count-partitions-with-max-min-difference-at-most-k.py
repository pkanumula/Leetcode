from typing import List
from collections import deque

MOD = 10**9 + 7

class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        # dp[i] = number of ways to partition nums[0..i-1]
        dp = [0] * (n + 1)
        # pref[i] = sum of dp[0..i] modulo MOD
        pref = [0] * (n + 1)
        
        dp[0] = 1
        pref[0] = 1
        
        minq = deque()  # indices, increasing values (for min)
        maxq = deque()  # indices, decreasing values (for max)
        
        l = 0  # left boundary of the valid window
        
        for i, x in enumerate(nums):
            # Insert into min queue
            while minq and nums[minq[-1]] >= x:
                minq.pop()
            minq.append(i)
            
            # Insert into max queue
            while maxq and nums[maxq[-1]] <= x:
                maxq.pop()
            maxq.append(i)
            
            # Shrink from the left until condition satisfied
            while nums[maxq[0]] - nums[minq[0]] > k:
                l += 1
                if minq[0] < l:
                    minq.popleft()
                if maxq[0] < l:
                    maxq.popleft()
            
            # Now all segments starting in [l..i] and ending at i are valid.
            # Last segment start index is j in [l..i], and contributes dp[j].
            # So dp[i+1] = sum_{j=l}^i dp[j]
            total = pref[i]
            if l > 0:
                total = (total - pref[l - 1]) % MOD
            
            dp[i + 1] = total
            pref[i + 1] = (pref[i] + dp[i + 1]) % MOD
        
        return dp[n]
