class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        from collections import Counter

        # Count total occurrences of each character
        total_count = Counter(s)
        # Check if it's possible to take at least k of each character
        if any(total_count[ch] < k for ch in 'abc'):
            return -1

        n = len(s)
        # Determine the maximum substring we can leave out while keeping at least k of each character
        required = {ch: total_count[ch] - k for ch in 'abc'}
        left_count = Counter()
        max_length = 0
        l = 0

        for r in range(n):
            left_count[s[r]] += 1
            # Check if the current window violates the required counts
            while any(left_count[ch] > required[ch] for ch in 'abc'):
                left_count[s[l]] -= 1
                l += 1
            # Update the maximum length of the valid window
            max_length = max(max_length, r - l + 1)

        # Minimum time is total length minus the maximum valid window length
        return n - max_length
