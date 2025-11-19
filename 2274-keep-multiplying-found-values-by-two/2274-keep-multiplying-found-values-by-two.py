class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        numset = set(nums)
        
        while original in numset:
            original *= 2
        
        return original
