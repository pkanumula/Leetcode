from typing import List

class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        # Base sum of original values
        base_sum = sum(nums)
        # Compute delta for toggling each node
        deltas = [(num ^ k) - num for num in nums]
        # Sort deltas in descending order
        deltas.sort(reverse=True)
        # Sum of positive deltas and count
        total_delta = 0
        pos_count = 0
        for d in deltas:
            if d > 0:
                total_delta += d
                pos_count += 1
            else:
                break
        # If even number of positives, take them all
        if pos_count % 2 == 0:
            return base_sum + total_delta
        # Otherwise, adjust by either removing smallest positive or adding largest non-positive
        # Find smallest positive delta
        smallest_pos = deltas[pos_count - 1]
        # Option1: drop smallest positive
        option1 = total_delta - smallest_pos
        # Find largest non-positive delta (<= 0)
        largest_non_pos = next((d for d in deltas[pos_count:] if d <= 0), None)
        if largest_non_pos is not None:
            option2 = total_delta + largest_non_pos
            best_delta = max(option1, option2)
        else:
            best_delta = option1
        return base_sum + best_delta