class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        steps = 0
        factor = 2
        
        while n > 1:
            while n % factor == 0:
                steps += factor
                n //= factor
            factor += 1
        
        return steps
