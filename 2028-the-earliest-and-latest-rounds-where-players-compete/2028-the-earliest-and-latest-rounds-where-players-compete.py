from functools import lru_cache
from typing import List

class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        # ensure a < b
        a0, b0 = min(firstPlayer, secondPlayer), max(firstPlayer, secondPlayer)

        @lru_cache(None)
        def dp(n: int, a: int, b: int) -> (int, int):
            # if they meet this round
            if a + b == n + 1:
                return (1, 1)

            # build the list of "other" matches (positions) this round
            m = n // 2
            pairs = [(i, n+1-i) for i in range(1, m+1)]
            # survivors from non-special bye if odd
            mid = (n+1)//2 if n%2 else None

            # remove any pair involving a or b
            other_pairs = []
            for i,j in pairs:
                if (i == a and j == b) or (i == b and j == a):
                    # this would have been the special-a vs special-b match,
                    # but we already handled a+b==n+1 above
                    continue
                if i==a or i==b or j==a or j==b:
                    # special matched with someone else → that match is not "other"
                    continue
                other_pairs.append((i,j))

            # does a non-special middle bye survive?
            has_mid = (mid is not None and mid != a and mid != b)

            next_states = set()
            K = len(other_pairs)
            # iterate all 2^K ways to pick one winner from each other match
            for mask in range(1<<K):
                survivors = [a, b]
                if has_mid:
                    survivors.append(mid)
                # pick one from each other match
                for t in range(K):
                    i,j = other_pairs[t]
                    survivors.append(j if (mask>>t)&1 else i)
                survivors.sort()
                # build next (a',b') in sorted survivors
                n2 = len(survivors)
                # index() is safe because a and b definitely in list
                a2 = survivors.index(a) + 1
                b2 = survivors.index(b) + 1
                next_states.add((n2, a2, b2))

            # recurse into all children
            min_round = float('inf')
            max_round = 0
            for (n2, a2, b2) in next_states:
                e, l = dp(n2, a2, b2)
                min_round = min(min_round, e)
                max_round = max(max_round, l)

            # they meet this round + after
            return (min_round + 1, max_round + 1)

        return list(dp(n, a0, b0))
