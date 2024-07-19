class Solution(object):
    def threeConsecutiveOdds(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        # Initialize a counter for consecutive odd numbers
        consecutive_odds = 0
        
        # Iterate through the array
        for num in arr:
            # Check if the current number is odd
            if num % 2 == 1:
                consecutive_odds += 1
                # If we have found three consecutive odd numbers, return True
                if consecutive_odds == 3:
                    return True
            else:
                # Reset the counter if the current number is not odd
                consecutive_odds = 0
        
        # If we complete the loop without finding three consecutive odd numbers, return False
        return False

        