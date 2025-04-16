from collections import defaultdict

class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        pair_count = 0
        res = 0
        left = 0

        for right in range(len(nums)):
            pair_count += count[nums[right]]
            count[nums[right]] += 1

            while pair_count >= k:
                res += len(nums) - right
                count[nums[left]] -= 1
                pair_count -= count[nums[left]]
                left += 1

        return res
