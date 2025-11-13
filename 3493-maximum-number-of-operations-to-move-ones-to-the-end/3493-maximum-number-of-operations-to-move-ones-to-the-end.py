class Solution:
    def maxOperations(self, s: str) -> int:
        ans = 0
        ones = 0
        i = 0
        n = len(s)
        
        while i < n:
            if s[i] == '1':
                ones += 1
                i += 1
            else:
                # We encountered a '0'.
                # All '1's seen so far can perform an operation to cross this gap.
                ans += ones
                
                # Skip all consecutive '0's because crossing 1 zero 
                # or 100 zeros in a row counts as a single operation.
                while i < n and s[i] == '0':
                    i += 1
                    
        return ans