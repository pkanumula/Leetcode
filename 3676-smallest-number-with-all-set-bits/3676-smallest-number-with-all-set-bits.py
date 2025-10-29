class Solution:
    def smallestNumber(self, n: int) -> int:
        # Smallest number >= n with all bits set (e.g., 1, 3, 7, 15, ...)
        return (1 << n.bit_length()) - 1
