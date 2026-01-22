from typing import List

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        def is_nondecreasing(arr: List[int]) -> bool:
            return all(arr[i] >= arr[i - 1] for i in range(1, len(arr)))

        ops = 0

        while not is_nondecreasing(nums):
            # find leftmost adjacent pair with minimum sum
            min_sum = float("inf")
            idx = 0
            for i in range(len(nums) - 1):
                s = nums[i] + nums[i + 1]
                if s < min_sum:   # strictly < ensures leftmost on ties
                    min_sum = s
                    idx = i

            # replace that pair with their sum
            nums[idx:idx + 2] = [min_sum]
            ops += 1

        return ops
