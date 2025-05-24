from typing import List

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        # Enumerate over words, keeping index i and word w,
        # and include i in the result if x is found in w
        return [i for i, w in enumerate(words) if x in w]
