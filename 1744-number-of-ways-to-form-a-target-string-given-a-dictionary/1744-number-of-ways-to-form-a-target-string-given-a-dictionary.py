from collections import Counter
from functools import lru_cache

class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        MOD = 10**9 + 7
        word_len = len(words[0])
        target_len = len(target)

        # Precompute the frequency of each character at each position
        char_count = [Counter() for _ in range(word_len)]
        for word in words:
            for i, char in enumerate(word):
                char_count[i][char] += 1

        @lru_cache(None)
        def dfs(i, j):
            # If we completed the target
            if j == target_len:
                return 1

            # If we ran out of characters in the words
            if i == word_len:
                return 0

            # Skip current position in words
            ways = dfs(i + 1, j) % MOD

            # Use current character if it matches target[j]
            if target[j] in char_count[i]:
                ways += char_count[i][target[j]] * dfs(i + 1, j + 1)
                ways %= MOD

            return ways

        return dfs(0, 0)
