from collections import Counter

class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        # Combine the two sentences into one list of words
        words = s1.split() + s2.split()
        
        # Count the frequency of each word
        count = Counter(words)
        
        # Return the words that appear exactly once
        return [word for word in count if count[word] == 1]
