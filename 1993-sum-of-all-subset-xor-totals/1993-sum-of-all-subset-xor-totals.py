class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result |= num * (1 << (len(nums) - 1))
        return result
