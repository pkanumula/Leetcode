class Solution:
    def totalMoney(self, n: int) -> int:
        weeks = n // 7       # Number of full weeks
        days = n % 7         # Remaining days in the last (partial) week
        
        # Total from full weeks: arithmetic series sum per week
        # Week 1: 1+2+3+4+5+6+7 = 28
        # Week 2: 2+3+4+5+6+7+8 = 35
        # Each next week increases total by 7
        total = (weeks * 28) + (7 * (weeks * (weeks - 1)) // 2)
        
        # Add remaining days from the partial week
        for d in range(days):
            total += weeks + d + 1
        
        return total
