class Solution(object):
    def xorQueries(self, arr, queries):
        """
        :type arr: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        # Step 1: Precompute the prefix XOR array
        n = len(arr)
        prefix = [0] * (n + 1)
        
        for i in range(n):
            prefix[i + 1] = prefix[i] ^ arr[i]
        
        # Step 2: Answer each query using the prefix XOR array
        result = []
        for left, right in queries:
            result.append(prefix[right + 1] ^ prefix[left])
        
        return result
