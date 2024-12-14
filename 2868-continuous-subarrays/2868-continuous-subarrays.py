from collections import deque

class Solution:
    def continuousSubarrays(self, nums: list[int]) -> int:
        n = len(nums)
        left = 0
        result = 0
        max_deque = deque()  # Stores indices for the max values in the current window
        min_deque = deque()  # Stores indices for the min values in the current window

        for right in range(n):
            # Update max_deque
            while max_deque and nums[max_deque[-1]] < nums[right]:
                max_deque.pop()
            max_deque.append(right)

            # Update min_deque
            while min_deque and nums[min_deque[-1]] > nums[right]:
                min_deque.pop()
            min_deque.append(right)

            # Check the condition |nums[max] - nums[min]| <= 2
            while nums[max_deque[0]] - nums[min_deque[0]] > 2:
                left += 1
                if max_deque[0] < left:
                    max_deque.popleft()
                if min_deque[0] < left:
                    min_deque.popleft()

            # Add the number of subarrays ending at 'right'
            result += right - left + 1

        return result
