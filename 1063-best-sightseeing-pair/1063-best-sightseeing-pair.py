from typing import List

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        max_score = 0
        max_i = values[0]  # Keep track of the maximum value of values[i] + i

        for j in range(1, len(values)):
            # Update the maximum score using the current max_i
            max_score = max(max_score, max_i + values[j] - j)

            # Update max_i for the next iteration
            max_i = max(max_i, values[j] + j)

        return max_score