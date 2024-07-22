class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""

        def expand_around_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        longest = ""
        for i in range(len(s)):
            # Check for odd-length palindromes (single center)
            palindrome1 = expand_around_center(i, i)
            if len(palindrome1) > len(longest):
                longest = palindrome1

            # Check for even-length palindromes (double center)
            palindrome2 = expand_around_center(i, i + 1)
            if len(palindrome2) > len(longest):
                longest = palindrome2

        return longest
