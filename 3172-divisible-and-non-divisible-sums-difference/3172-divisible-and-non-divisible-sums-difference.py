class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        total_sum = n * (n + 1) // 2  # Sum of all numbers from 1 to n
        count_div_m = n // m
        sum_div_m = m * count_div_m * (count_div_m + 1) // 2  # Sum of all multiples of m up to n
        return total_sum - 2 * sum_div_m  # (sum_not_div_m = total_sum - sum_div_m), so result = total_sum - 2*sum_div_m
