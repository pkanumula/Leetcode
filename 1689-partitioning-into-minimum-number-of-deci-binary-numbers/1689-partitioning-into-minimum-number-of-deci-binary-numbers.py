class Solution:
    def minPartitions(self, n: str) -> int:
        # Minimum count equals the maximum digit in n
        return max(int(ch) for ch in n)