class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        if n == 0:
            return 0
        
        # Step 1: Give each child 1 candy initially
        candies = [1] * n
        
        # Step 2: Left-to-right pass
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        
        # Step 3: Right-to-left pass
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                # Take the maximum to preserve the left-to-right assignment
                candies[i] = max(candies[i], candies[i + 1] + 1)
        
        # Step 4: Total candies needed
        return sum(candies)
