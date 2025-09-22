from typing import List
from collections import Counter

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        cnt = Counter(nums)                      # frequency of each value [web:9]
        mx = max(cnt.values())                   # maximum frequency m [web:9]
        return sum(f for f in cnt.values() if f == mx)  # sum of all f == m [web:9][web:1]
