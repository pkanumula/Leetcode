from typing import List

class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0

        for i in range(n):
            # Optional pruning: if even taking whole suffix can't beat ans, stop.
            if n - i <= ans:
                break

            freq = {}
            distinct_even = 0
            distinct_odd = 0

            for j in range(i, n):
                x = nums[j]
                prev = freq.get(x, 0)

                if prev == 0:
                    if x & 1:
                        distinct_odd += 1
                    else:
                        distinct_even += 1

                freq[x] = prev + 1

                if distinct_even == distinct_odd:
                    ans = max(ans, j - i + 1)

        return ans
