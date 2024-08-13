class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def backtrack(start, target, path):
            if target == 0:
                result.append(path)
                return
            if target < 0:
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:  # Skip duplicates
                    continue
                backtrack(i + 1, target - candidates[i], path + [candidates[i]])

        candidates.sort()  # Sort candidates to handle duplicates and make it easier to skip them
        result = []
        backtrack(0, target, [])
        return result
