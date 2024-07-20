class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_set = set()  # To store characters in the current window
        start = 0  # Start pointer of the sliding window
        max_length = 0  # To keep track of the maximum length
        
        for end in range(len(s)):
            while s[end] in char_set:
                char_set.remove(s[start])  # Remove the character at `start`
                start += 1  # Move the start pointer to the right
            
            char_set.add(s[end])  # Add the current character to the set
            max_length = max(max_length, end - start + 1)  # Update the max length
        
        return max_length
