from collections import defaultdict

class Solution:
    def countPairs(self, nums: list[int], k: int) -> int:
        indices = defaultdict(list)
        for i, num in enumerate(nums):
            indices[num].append(i)

        count = 0
        for same_vals in indices.values():
            for i in range(len(same_vals)):
                for j in range(i + 1, len(same_vals)):
                    if (same_vals[i] * same_vals[j]) % k == 0:
                        count += 1
        return count
