class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Define a dictionary to map Roman numerals to their corresponding integer values
        roman_to_int = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        # Initialize the integer value
        integer_value = 0
        
        # Traverse the string
        for i in range(len(s)):
            # If the current numeral is less than the next numeral, subtract its value
            if i + 1 < len(s) and roman_to_int[s[i]] < roman_to_int[s[i + 1]]:
                integer_value -= roman_to_int[s[i]]
            else:
                # Otherwise, add its value
                integer_value += roman_to_int[s[i]]
        
        return integer_value