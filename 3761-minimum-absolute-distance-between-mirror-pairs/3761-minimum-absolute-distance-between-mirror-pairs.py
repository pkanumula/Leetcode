class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        def reverse(x):
            result = 0
            while x > 0:
                result = result * 10 + x % 10
                x //= 10
            return result
        
        seen = {}
        min_distance = float('inf')
        
        for i in range(len(nums)):
            if nums[i] in seen:
                distance = i - seen[nums[i]]
                min_distance = min(min_distance, distance)
            
            reversed_num = reverse(nums[i])
            seen[reversed_num] = i
        
        return min_distance if min_distance != float('inf') else -1