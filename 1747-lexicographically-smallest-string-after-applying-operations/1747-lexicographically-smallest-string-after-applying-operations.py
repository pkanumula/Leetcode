class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        from collections import deque

        def add_op(t: str) -> str:
            # add 'a' to digits at odd indices (0-indexed), modulo 10
            chars = list(t)
            for i in range(1, len(chars), 2):
                chars[i] = str((int(chars[i]) + a) % 10)
            return "".join(chars)

        def rotate_op(t: str) -> str:
            # rotate right by b
            k = b % len(t)
            return t[-k:] + t[:-k] if k else t

        seen = set([s])
        q = deque([s])
        ans = s

        while q:
            cur = q.popleft()
            if cur < ans:
                ans = cur

            nxt1 = add_op(cur)
            if nxt1 not in seen:
                seen.add(nxt1)
                q.append(nxt1)

            nxt2 = rotate_op(cur)
            if nxt2 not in seen:
                seen.add(nxt2)
                q.append(nxt2)

        return ans
