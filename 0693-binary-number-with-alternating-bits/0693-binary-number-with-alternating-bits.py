class Solution(object):
    def hasAlternatingBits(self, n):
        xor = n ^ (n >> 1)
        return (xor & (xor + 1)) == 0