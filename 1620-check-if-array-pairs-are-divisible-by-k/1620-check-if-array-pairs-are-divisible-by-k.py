class Solution(object):
    def canArrange(self, arr, k):
        remainder_count = [0] * k
        
        # Count the remainders when divided by k
        for num in arr:
            remainder_count[num % k] += 1
        
        # Check if remainder pairs can form divisible sums
        if remainder_count[0] % 2 != 0:
            return False
        
        for i in range(1, k):
            if remainder_count[i] != remainder_count[k - i]:
                return False
        
        return True
