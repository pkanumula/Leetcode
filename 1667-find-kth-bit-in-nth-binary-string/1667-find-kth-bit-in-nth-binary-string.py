class Solution(object):
    def findKthBit(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        # Function to find the k-th bit recursively
        def findBit(n, k):
            # Base case: if n is 1, the string S1 is "0"
            if n == 1:
                return '0'
            
            # Calculate the length of the current string Sn
            length = (1 << n) - 1  # 2^n - 1
            
            # Middle position in the current string
            mid = (length // 2) + 1
            
            if k == mid:
                return '1'
            elif k < mid:
                return findBit(n - 1, k)
            else:
                # k is in the second half, so we find the mirrored position
                # in the first half and invert the result
                return '1' if findBit(n - 1, length - k + 1) == '0' else '0'
        
        return findBit(n, k)
