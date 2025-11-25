class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        # If k shares a factor with 10 (i.e., 2 or 5), it's impossible
        if k % 2 == 0 or k % 5 == 0:
            return -1
        
        rem = 0
        for length in range(1, k + 1):
            rem = (rem * 10 + 1) % k
            if rem == 0:
                return length
        
        # Should never reach here if k is coprime with 10, but kept for completeness
        return -1
