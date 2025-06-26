class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        n = len(s)
        count = 0
        value = 0
        power = 1

        # Start from the end of the string
        for i in range(n - 1, -1, -1):
            if s[i] == '0':
                count += 1  # zero always allowed
            else:
                if power <= k and value + power <= k:
                    value += power
                    count += 1
                # Do not include if this '1' would push value over k
            power <<= 1  # equivalent to power *= 2
            if power > k:
                break  # any more 1s will overshoot k due to power being too large

        # Add all remaining leading zeros to count (they are "free" and don't affect value)
        for j in range(i - 1, -1, -1):
            if s[j] == '0':
                count += 1

        return count
