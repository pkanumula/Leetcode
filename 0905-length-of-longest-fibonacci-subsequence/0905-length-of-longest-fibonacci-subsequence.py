from typing import List

class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        index = {num: i for i, num in enumerate(arr)}  # Mapping number to index
        dp = {}  # Stores (i, j) -> length of sequence ending at i, j
        max_length = 0

        for j in range(len(arr)):
            for i in range(j):
                x = arr[j] - arr[i]
                if x < arr[i] and x in index:
                    k = index[x]
                    dp[(i, j)] = dp.get((k, i), 2) + 1
                    max_length = max(max_length, dp[(i, j)])

        return max_length if max_length >= 3 else 0
