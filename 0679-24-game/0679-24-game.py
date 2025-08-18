from typing import List

class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        EPS = 1e-6

        def dfs(nums: List[float]) -> bool:
            if len(nums) == 1:
                return abs(nums[0] - 24) < EPS

            # Try all unordered pairs (i, j), i != j
            n = len(nums)
            for i in range(n):
                for j in range(n):
                    if i == j:
                        continue

                    a, b = nums[i], nums[j]
                    # Remaining numbers after removing i and j
                    rest = [nums[k] for k in range(n) if k != i and k != j]

                    # Generate next candidates from a and b
                    next_vals = [
                        a + b,
                        a - b,
                        b - a,
                        a * b
                    ]
                    if abs(b) > EPS:
                        next_vals.append(a / b)
                    if abs(a) > EPS:
                        next_vals.append(b / a)

                    for val in next_vals:
                        if dfs(rest + [val]):
                            return True
            return False

        # Start with floats to handle real division
        return dfs([float(x) for x in cards])
