from collections import Counter

class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        freq = list(Counter(word).values())
        freq.sort()
        n = len(freq)
        prefix_sum = [0] * (n + 1)

        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + freq[i]

        res = float('inf')
        for i in range(n):
            min_freq = freq[i]
            max_allowed = min_freq + k
            # Binary search to find rightmost index with freq <= max_allowed
            l, r = i, n - 1
            while l <= r:
                mid = (l + r) // 2
                if freq[mid] <= max_allowed:
                    l = mid + 1
                else:
                    r = mid - 1
            # i is start index, r is the last index satisfying condition
            to_keep = prefix_sum[r + 1] - prefix_sum[i]
            to_delete = prefix_sum[i] + (prefix_sum[n] - prefix_sum[r + 1] - (n - r - 1) * max_allowed)
            res = min(res, to_delete)

        return res
