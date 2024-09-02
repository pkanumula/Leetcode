class Solution(object):
    def chalkReplacer(self, chalk, k):
        """
        :type chalk: List[int]
        :type k: int
        :rtype: int
        """
        total_chalk = sum(chalk)
        k = k % total_chalk
        
        for i in range(len(chalk)):
            if chalk[i] > k:
                return i
            k -= chalk[i]