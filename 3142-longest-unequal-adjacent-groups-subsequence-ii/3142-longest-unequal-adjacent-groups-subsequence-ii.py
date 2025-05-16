from typing import List

class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(words)
        
        def hamming1(a: str, b: str) -> bool:
            # same length and exactly 1 mismatch
            if len(a) != len(b):
                return False
            diff = 0
            for x, y in zip(a, b):
                if x != y:
                    diff += 1
                    if diff > 1:
                        return False
            return diff == 1
        
        # dp[i] = [length of best subseq ending at i, previous index]
        dp = [[1, -1] for _ in range(n)]
        
        for i in range(n):
            for j in range(i):
                if groups[i] != groups[j] and hamming1(words[j], words[i]):
                    if dp[j][0] + 1 > dp[i][0]:
                        dp[i] = [dp[j][0] + 1, j]
        
        # find end of longest
        end = max(range(n), key=lambda i: dp[i][0])
        seq = []
        while end != -1:
            seq.append(words[end])
            end = dp[end][1]
        
        return seq[::-1]
