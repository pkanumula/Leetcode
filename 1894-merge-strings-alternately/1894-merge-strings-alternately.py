class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        # Initialize an empty list to collect the merged characters
        merged = []
        
        # Get the length of the shorter word
        min_length = min(len(word1), len(word2))
        
        # Add characters in alternating order up to the length of the shorter word
        for i in range(min_length):
            merged.append(word1[i])
            merged.append(word2[i])
        
        # Append the remaining characters of the longer word
        if len(word1) > len(word2):
            merged.append(word1[min_length:])
        else:
            merged.append(word2[min_length:])
        
        # Join the list into a single string and return it
        return ''.join(merged)
