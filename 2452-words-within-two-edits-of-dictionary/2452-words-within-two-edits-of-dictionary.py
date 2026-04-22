class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        result = []
        for query in queries:
            for word in dictionary:
                # Count positions where characters differ
                diffs = sum(q != d for q, d in zip(query, word))
                if diffs <= 2:
                    result.append(query)
                    break  # No need to check other dictionary words
        return result