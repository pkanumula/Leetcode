class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        
        # Create a new string that helps to find the longest palindromic prefix
        rev_s = s[::-1]  # Reverse of the string
        new_s = s + '#' + rev_s  # s + '#' + reverse of s (to avoid overlap)
        
        # Create a KMP table (lps array) for the new_s
        n = len(new_s)
        lps = [0] * n  # Longest prefix suffix array
        
        # Build the LPS array (same as KMP preprocessing)
        for i in range(1, n):
            j = lps[i - 1]
            while j > 0 and new_s[i] != new_s[j]:
                j = lps[j - 1]
            if new_s[i] == new_s[j]:
                j += 1
            lps[i] = j
        
        # The length of the longest palindromic prefix is lps[-1]
        # Add the remaining suffix (non-palindromic part) in front of s
        return rev_s[:len(s) - lps[-1]] + s
