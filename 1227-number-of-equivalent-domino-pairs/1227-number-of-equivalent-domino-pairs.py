from collections import defaultdict

class Solution:
    def numEquivDominoPairs(self, dominoes):
        count = defaultdict(int)
        res = 0
        for a, b in dominoes:
            key = tuple(sorted((a, b)))
            res += count[key]
            count[key] += 1
        return res
