from typing import List
import bisect

class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        positions = [pos for pos, _ in fruits]
        amounts = [amount for _, amount in fruits]
        n = len(fruits)

        # Prefix sums for amounts
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + amounts[i]

        def get_sum(left: int, right: int) -> int:
            # Sum of fruits in fruits[left:right+1]
            return prefix[right + 1] - prefix[left]

        max_fruits = 0

        # We will try all intervals and check feasibility
        # We do two pointer on positions array for left and right indexes
        j = 0
        for i in range(n):
            # Increase j while total steps to cover fruits[i..j] <= k
            while j < n:
                left_pos = positions[i]
                right_pos = positions[j]

                # Calculate minimum steps to cover from startPos
                # Two scenarios:
                dist_left_first = abs(startPos - left_pos) + (right_pos - left_pos)  # Go left first then right
                dist_right_first = abs(right_pos - startPos) + (right_pos - left_pos)  # Go right first then left

                min_steps = min(dist_left_first, dist_right_first)

                if min_steps <= k:
                    j += 1
                else:
                    break

            # Now interval is fruits[i..j-1] because j went one too far
            if j - 1 >= i:
                total = get_sum(i, j - 1)
                if total > max_fruits:
                    max_fruits = total

        return max_fruits
