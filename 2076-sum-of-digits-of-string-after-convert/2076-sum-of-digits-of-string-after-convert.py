class Solution(object):
    def getLucky(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # Step 1: Convert each letter in the string to its corresponding position in the alphabet
        numeric_string = ''.join(str(ord(char) - ord('a') + 1) for char in s)
        
        # Step 2: Convert the numeric string to an integer and sum the digits
        current_sum = sum(int(digit) for digit in numeric_string)
        
        # Step 3: Perform the transformation k-1 more times
        for _ in range(k - 1):
            current_sum = sum(int(digit) for digit in str(current_sum))
        
        return current_sum
