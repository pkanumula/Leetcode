class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # Negative numbers are not palindromes
        if x < 0:
            return False
        
        # If x is not 0 and ends with 0, it's not a palindrome
        if x != 0 and x % 10 == 0:
            return False
        
        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10
        
        # When the length is odd, we can get rid of the middle digit by reversed_half//10
        return x == reversed_half or x == reversed_half // 10