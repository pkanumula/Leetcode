class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        i, n = 0, len(s)
        
        # Skip whitespace
        while i < n and s[i] == ' ':
            i += 1
        
        # Check sign
        sign = 1
        if i < n and (s[i] == '+' or s[i] == '-'):
            sign = -1 if s[i] == '-' else 1
            i += 1
        
        # Convert digits
        result = 0
        while i < n and s[i].isdigit():
            digit = ord(s[i]) - ord('0')
            
            # Check for overflow
            if result > (2**31 - 1 - digit) // 10:
                return 2**31 - 1 if sign == 1 else -2**31
            
            result = result * 10 + digit
            i += 1
        
        return sign * result