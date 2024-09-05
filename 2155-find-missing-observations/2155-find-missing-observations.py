class Solution(object):
    def missingRolls(self, rolls, mean, n):
        """
        :type rolls: List[int]
        :type mean: int
        :type n: int
        :rtype: List[int]
        """
        m = len(rolls)
        total_sum = mean * (n + m)  # Total expected sum
        sum_of_rolls = sum(rolls)  # Sum of the known rolls
        
        missing_sum = total_sum - sum_of_rolls  # Sum of missing rolls
        
        # Check if the missing sum is within the possible range
        if missing_sum < n or missing_sum > 6 * n:
            return []
        
        # Create the missing array
        missing_rolls = [1] * n
        missing_sum -= n  # Start by assuming each roll is 1
        
        # Distribute the remaining missing_sum
        for i in range(n):
            if missing_sum == 0:
                break
            add = min(5, missing_sum)  # We can add at most 5 to any roll (1 + 5 = 6)
            missing_rolls[i] += add
            missing_sum -= add
        
        return missing_rolls
