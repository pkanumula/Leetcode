from collections import Counter

class Solution:
    def maximumBeauty(self, nums: list[int], k: int) -> int:
        events = []

        # Create events for range [nums[i] - k, nums[i] + k]
        for num in nums:
            events.append((num - k, 1))  # Start of range
            events.append((num + k + 1, -1))  # End of range (exclusive)

        # Sort events by position, breaking ties by type of event
        events.sort()

        # Sweep line to find the maximum overlap
        current_beauty = 0
        max_beauty = 0

        for _, change in events:
            current_beauty += change
            max_beauty = max(max_beauty, current_beauty)

        return max_beauty