from typing import List

class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)
        # Reuse energy as dp to get O(1) extra space:
        # After processing, energy[i] holds dp[i].
        for i in range(n - 1, -1, -1):
            if i + k < n:
                energy[i] += energy[i + k]
        return max(energy)
