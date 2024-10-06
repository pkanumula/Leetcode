class Solution(object):
    def areSentencesSimilar(self, sentence1, sentence2):
        """
        :type sentence1: str
        :type sentence2: str
        :rtype: bool
        """
        words1 = sentence1.split()
        words2 = sentence2.split()
        
        # Ensure words1 is the shorter sentence for simplicity
        if len(words1) > len(words2):
            words1, words2 = words2, words1
        
        i, j = 0, len(words1) - 1
        m, n = 0, len(words2) - 1
        
        # Check prefix similarity
        while i <= j and words1[i] == words2[m]:
            i += 1
            m += 1
        
        # Check suffix similarity
        while i <= j and words1[j] == words2[n]:
            j -= 1
            n -= 1
        
        # If all words in the shorter sentence have been matched, return True
        return i > j
