class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def backtrack(index, seen):
            if index == len(s):
                return 0
            max_splits = 0
            for end in range(index + 1, len(s) + 1):
                substring = s[index:end]
                if substring not in seen:
                    seen.add(substring)
                    max_splits = max(max_splits, 1 + backtrack(end, seen))
                    seen.remove(substring)
            return max_splits
        
        return backtrack(0, set())