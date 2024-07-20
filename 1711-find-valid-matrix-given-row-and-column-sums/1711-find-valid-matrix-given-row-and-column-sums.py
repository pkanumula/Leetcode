class Solution(object):
    def restoreMatrix(self, rowSum, colSum):
        """
        :type rowSum: List[int]
        :type colSum: List[int]
        :rtype: List[List[int]]
        """
        m, n = len(rowSum), len(colSum)
        matrix = [[0] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                # The value to be placed in matrix[i][j] is the minimum of rowSum[i] and colSum[j]
                matrix[i][j] = min(rowSum[i], colSum[j])
                
                # Subtract the placed value from rowSum and colSum
                rowSum[i] -= matrix[i][j]
                colSum[j] -= matrix[i][j]
                
        return matrix
