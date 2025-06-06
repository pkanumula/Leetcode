class Solution:
    def robotWithString(self, s: str) -> str:
        from collections import deque

        # Precompute suffix minimums
        n = len(s)
        min_suff = [''] * n
        min_suff[-1] = s[-1]
        for i in range(n - 2, -1, -1):
            min_suff[i] = min(s[i], min_suff[i + 1])

        t = []  # Stack
        result = []  # Final output string
        for i in range(n):
            t.append(s[i])
            # Pop from t to result if top of t <= min of remaining s
            while t and (i == n - 1 or t[-1] <= min_suff[i + 1]):
                result.append(t.pop())

        # Any remaining in t can be popped now
        while t:
            result.append(t.pop())

        return ''.join(result)
