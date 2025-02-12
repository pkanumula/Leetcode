from collections import defaultdict

class Solution:
    def maximumSum(self, nums):
        digit_sum_map = defaultdict(int)
        max_sum = -1

        for num in nums:
            digit_sum = sum(int(d) for d in str(num))
            if digit_sum in digit_sum_map:
                max_sum = max(max_sum, digit_sum_map[digit_sum] + num)
                digit_sum_map[digit_sum] = max(digit_sum_map[digit_sum], num)
            else:
                digit_sum_map[digit_sum] = num

        return max_sum
