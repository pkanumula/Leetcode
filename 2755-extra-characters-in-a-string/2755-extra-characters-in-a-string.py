class Solution(object):
    def minExtraChar(self, s, dictionary):
        """
        :type s: str
        :type dictionary: List[str]
        :rtype: int
        """
        n = len(s)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        word_set = set(dictionary)
        
        for i in range(1, n + 1):
            dp[i] = dp[i - 1] + 1  # assume character s[i-1] is extra
            for j in range(i):
                if s[j:i] in word_set:
                    dp[i] = min(dp[i], dp[j])
        
        return dp[n]
