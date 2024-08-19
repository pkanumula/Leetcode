class Solution(object):
    def smallestTrimmedNumbers(self, nums, queries):
        """
        :type nums: List[str]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        n, m = len(nums), len(queries)
        answer = [0] * m
        
        # Precompute the index of the kth smallest trimmed number for each trim length
        index = [[] for _ in range(101)]
        for i, num in enumerate(nums):
            for trim in range(1, len(num) + 1):
                key = int(num[-trim:])
                index[trim].append((key, i))
        for trim in range(1, 101):
            index[trim].sort()
        
        # Process the queries
        for i, (k, trim) in enumerate(queries):
            answer[i] = index[trim][k - 1][1]
        
        return answer