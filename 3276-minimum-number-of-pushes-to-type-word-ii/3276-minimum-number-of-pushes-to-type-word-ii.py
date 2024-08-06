from collections import Counter

class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        # Count the frequency of each character in the word
        char_freq = Counter(word)
        
        # Sort characters by frequency in descending order
        sorted_chars = sorted(char_freq.items(), key=lambda x: x[1], reverse=True)
        
        total_pushes = 0
        for i, (char, freq) in enumerate(sorted_chars):
            # Calculate the number of pushes needed for this character
            pushes = ((i // 8) + 1) * freq
            total_pushes += pushes
        
        return total_pushes