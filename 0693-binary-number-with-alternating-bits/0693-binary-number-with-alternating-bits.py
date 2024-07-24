class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # XOR n with n >> 1
        xor = n ^ (n >> 1)
        
        # Check if xor is all 1s
        return (xor & (xor + 1)) == 0