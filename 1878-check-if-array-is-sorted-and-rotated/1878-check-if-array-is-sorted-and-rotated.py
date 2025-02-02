class Solution:
    def check(self, nums: list[int]) -> bool:
        # Count the number of places where the next element is less than the current one
        count_decrease = 0
        n = len(nums)
        
        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                count_decrease += 1
                if count_decrease > 1:
                    return False
        
        return True
