from typing import List

class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        # Calculate the sum of every k-length window
        window_sums = [sum(nums[:k])]
        for i in range(1, n - k + 1):
            window_sums.append(window_sums[-1] - nums[i - 1] + nums[i + k - 1])

        # Arrays to store the best left and right indices
        left = [0] * len(window_sums)
        right = [0] * len(window_sums)

        # Fill the left array
        best_left = 0
        for i in range(len(window_sums)):
            if window_sums[i] > window_sums[best_left]:
                best_left = i
            left[i] = best_left

        # Fill the right array
        best_right = len(window_sums) - 1
        for i in range(len(window_sums) - 1, -1, -1):
            if window_sums[i] >= window_sums[best_right]:  # Use >= for lexicographically smallest
                best_right = i
            right[i] = best_right

        # Find the max sum by iterating over the middle subarray
        max_sum = 0
        result = []
        for mid in range(k, len(window_sums) - k):
            l, r = left[mid - k], right[mid + k]
            curr_sum = window_sums[l] + window_sums[mid] + window_sums[r]
            if curr_sum > max_sum:
                max_sum = curr_sum
                result = [l, mid, r]

        return result
