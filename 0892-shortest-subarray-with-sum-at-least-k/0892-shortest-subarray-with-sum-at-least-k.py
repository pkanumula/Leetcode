from collections import deque

class Solution:
    def shortestSubarray(self, nums: list[int], k: int) -> int:
        n = len(nums)
        prefix_sum = [0] * (n + 1)

        # Compute the prefix sum
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]

        # Deque to maintain indices
        dq = deque()
        result = float('inf')

        for i in range(n + 1):
            # Check if we can form a valid subarray
            while dq and prefix_sum[i] - prefix_sum[dq[0]] >= k:
                result = min(result, i - dq.popleft())

            # Maintain the deque for increasing prefix sums
            while dq and prefix_sum[i] <= prefix_sum[dq[-1]]:
                dq.pop()

            # Add the current index to the deque
            dq.append(i)

        return result if result != float('inf') else -1