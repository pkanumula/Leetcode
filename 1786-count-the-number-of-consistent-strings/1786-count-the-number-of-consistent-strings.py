class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        # Convert allowed characters to a set for O(1) lookups
        allowed_set = set(allowed)
        
        # Count how many words are consistent
        consistent_count = 0
        
        for word in words:
            # Check if all characters in the word are in allowed_set
            if all(char in allowed_set for char in word):
                consistent_count += 1
                
        return consistent_count
