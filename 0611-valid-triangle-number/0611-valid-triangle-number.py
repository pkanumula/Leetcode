from typing import List

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        # Sort to enable two-pointer counting
        nums.sort()
        n = len(nums)
        count = 0

        # Fix the largest side at index k, and find pairs (i, j) < k
        for k in range(n - 1, 1, -1):
            # If the largest side is 0, no triangle can be formed with it
            if nums[k] == 0:
                continue
            i, j = 0, k - 1
            while i < j:
                # For sorted nums, if nums[i] + nums[j] > nums[k],
                # then all i..(j-1) with j form valid triangles with k.
                if nums[i] + nums[j] > nums[k]:
                    count += (j - i)
                    j -= 1
                else:
                    i += 1

        return count
