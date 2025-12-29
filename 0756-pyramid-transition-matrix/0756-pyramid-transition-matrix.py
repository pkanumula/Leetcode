from typing import List
from collections import defaultdict

class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        # Map pair -> possible tops
        nxt = defaultdict(set)
        for tri in allowed:
            nxt[tri[0] + tri[1]].add(tri[2])

        memo = {}  # row_string -> bool

        def can_build(row: str) -> bool:
            if len(row) == 1:
                return True
            if row in memo:
                return memo[row]

            # Build all possible next rows via DFS
            def build_next(i: int, acc: List[str]) -> bool:
                if i == len(row) - 1:
                    return can_build("".join(acc))

                pair = row[i] + row[i + 1]
                if pair not in nxt:
                    return False

                for top in nxt[pair]:
                    acc.append(top)
                    if build_next(i + 1, acc):
                        return True
                    acc.pop()
                return False

            memo[row] = build_next(0, [])
            return memo[row]

        return can_build(bottom)
