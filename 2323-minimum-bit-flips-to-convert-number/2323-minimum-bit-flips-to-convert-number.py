class Solution(object):
    def minBitFlips(self, start, goal):
        """
        :type start: int
        :type goal: int
        :rtype: int
        """
        # XOR start and goal to find positions where bits differ
        xor_result = start ^ goal
        
        # Count the number of 1s in the XOR result (which are the differing bits)
        return bin(xor_result).count('1')
