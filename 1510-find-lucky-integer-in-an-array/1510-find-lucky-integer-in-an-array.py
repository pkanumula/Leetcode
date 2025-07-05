from collections import Counter
from typing import List

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = Counter(arr)  # Count frequency of each number
        lucky = [num for num, count in freq.items() if num == count]  # Find all lucky numbers
        return max(lucky) if lucky else -1  # Return the largest lucky number, or -1 if none
