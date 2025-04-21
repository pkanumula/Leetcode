class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        min_sum = 0
        max_sum = 0
        current = 0

        for diff in differences:
            current += diff
            min_sum = min(min_sum, current)
            max_sum = max(max_sum, current)

        return max(0, (upper - lower) - (max_sum - min_sum) + 1)
