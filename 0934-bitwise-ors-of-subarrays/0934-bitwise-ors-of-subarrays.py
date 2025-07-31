from typing import List

class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        res = set()
        prev = set()
        
        for x in arr:
            curr = {x}
            for p in prev:
                curr.add(p | x)
            res |= curr
            prev = curr
        
        return len(res)
