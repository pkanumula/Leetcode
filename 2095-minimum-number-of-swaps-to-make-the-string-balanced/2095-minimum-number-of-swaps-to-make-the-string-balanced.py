class Solution(object):
    def minSwaps(self, s):
        """
        :type s: str
        :rtype: int
        """
        imbalance = 0  # Tracks the number of imbalanced closing brackets
        open_count = 0  # Tracks the number of opening brackets '['
        
        for char in s:
            if char == '[':
                open_count += 1  # Count opening brackets
            else:
                if open_count > 0:
                    open_count -= 1  # Match a closing bracket with an opening bracket
                else:
                    imbalance += 1  # Imbalance found, need to swap later
        
        # Every 2 imbalanced closing brackets require 1 swap
        return (imbalance + 1) // 2
