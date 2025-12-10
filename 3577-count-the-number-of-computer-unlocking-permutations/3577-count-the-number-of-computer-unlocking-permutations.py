from typing import List

MOD = 10**9 + 7

class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        n = len(complexity)
        
        root = complexity[0]
        # Check that complexity[0] is the unique global minimum
        for i in range(1, n):
            if complexity[i] <= root:
                return 0
        
        # Compute (n-1)! % MOD
        res = 1
        for k in range(2, n):
            res = (res * k) % MOD
        
        return res
