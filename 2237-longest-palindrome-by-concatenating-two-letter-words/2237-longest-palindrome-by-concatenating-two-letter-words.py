from collections import Counter
from typing import List

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        word_count = Counter(words)
        length = 0
        used_center = False

        for word in list(word_count.keys()):
            rev = word[::-1]

            if word != rev:
                pair_count = min(word_count[word], word_count[rev])
                length += pair_count * 4
                word_count[word] -= pair_count
                word_count[rev] -= pair_count
            else:
                pair_count = word_count[word] // 2
                length += pair_count * 4
                word_count[word] -= pair_count * 2

        for word in word_count:
            if word[0] == word[1] and word_count[word] > 0:
                length += 2
                break

        return length
