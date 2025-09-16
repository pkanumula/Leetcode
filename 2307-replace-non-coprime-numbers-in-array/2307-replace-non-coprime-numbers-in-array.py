from typing import List
from math import gcd

class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        st = []
        for x in nums:
            curr = x
            # Merge with stack top while non-coprime
            while st:
                g = gcd(st[-1], curr)
                if g == 1:
                    break
                # merge two numbers into their LCM
                curr = (st[-1] // g) * curr
                st.pop()
            st.append(curr)
        return st
