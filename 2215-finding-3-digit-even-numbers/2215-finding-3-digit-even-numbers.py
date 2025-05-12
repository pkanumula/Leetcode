from collections import Counter
from typing import List

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        count = Counter(digits)
        result = set()

        # Iterate through all possible 3-digit numbers
        for i in range(100, 1000):
            if i % 2 == 1:
                continue  # Skip odd numbers

            d1, d2, d3 = i // 100, (i // 10) % 10, i % 10
            current_count = Counter([d1, d2, d3])

            # Check if the number can be formed using the given digits
            if all(count[d] >= current_count[d] for d in current_count):
                result.add(i)

        return sorted(result)
