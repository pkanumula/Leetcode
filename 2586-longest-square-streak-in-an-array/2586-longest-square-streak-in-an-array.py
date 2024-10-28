class Solution:
    def longestSquareStreak(self, nums: list[int]) -> int:
        num_set = set(nums)
        max_streak = -1

        for num in nums:
            streak = 1
            while num * num in num_set:
                num *= num
                streak += 1
            if streak > 1:
                max_streak = max(max_streak, streak)

        return max_streak
