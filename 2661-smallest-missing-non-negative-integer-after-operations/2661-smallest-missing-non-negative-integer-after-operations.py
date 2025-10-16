from typing import List
from collections import Counter

class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        # Count residues modulo value
        cnt = Counter(x % value for x in nums)
        
        k = 0
        while True:
            r = k % value
            if cnt[r] > 0:
                cnt[r] -= 1   # use one number from this residue class to realize k
                k += 1
            else:
                return k
