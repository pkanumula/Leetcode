class Solution(object):
    def construct2DArray(self, original, m, n):
        """
        :type original: List[int]
        :type m: int
        :type n: int
        :rtype: List[List[int]]
        """
        # Check if it's possible to form the m x n array
        if len(original) != m * n:
            return []
        
        # Use list comprehension to efficiently create the 2D array
        return [original[i * n : (i + 1) * n] for i in range(m)]
