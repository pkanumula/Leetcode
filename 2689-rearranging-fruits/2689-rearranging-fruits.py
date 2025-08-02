from collections import Counter
from typing import List

class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        n = len(basket1)
        freq = Counter()
        for x in basket1:
            freq[x] += 1
        for x in basket2:
            freq[x] += 1

        # Check if total count of each fruit is even
        for v in freq.values():
            if v % 2 != 0:
                return -1

        # Count frequencies in each basket
        freq1 = Counter(basket1)
        freq2 = Counter(basket2)

        # Calculate excess fruits in basket1 and basket2 to be swapped
        excess1 = []
        excess2 = []

        for fruit in freq:
            diff = freq1[fruit] - freq2[fruit]
            if diff > 0:
                # diff/2 fruits need to be swapped out of basket1
                excess1.extend([fruit] * (diff // 2))
            elif diff < 0:
                # (-diff)/2 fruits need to be swapped out of basket2
                excess2.extend([fruit] * ((-diff) // 2))

        excess1.sort()
        excess2.sort()

        min_fruit = min(freq.keys())
        cost = 0
        # Swap pairs greedily
        for i in range(len(excess1)):
            # Cost of swapping these two fruits directly
            direct_swap_cost = min(excess1[i], excess2[-(i+1)])
            # Cost of swapping using minimal fruit as intermediary (2*min_fruit)
            cost += min(direct_swap_cost, 2 * min_fruit)

        return cost
