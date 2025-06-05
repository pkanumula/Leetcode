class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        # Initialize Union-Find parent pointers for 'a'..'z'
        parent = list(range(26))

        def find(x: int) -> int:
            # Path compression
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x: int, y: int) -> None:
            # Find roots
            rx, ry = find(x), find(y)
            if rx == ry:
                return
            # Attach the larger root to the smaller root
            if rx < ry:
                parent[ry] = rx
            else:
                parent[rx] = ry

        # Step 1: Build equivalences from s1, s2
        for c1, c2 in zip(s1, s2):
            union(ord(c1) - ord('a'), ord(c2) - ord('a'))

        # Step 2: Build result for baseStr
        ans_chars = []
        for c in baseStr:
            r = find(ord(c) - ord('a'))
            ans_chars.append(chr(r + ord('a')))

        return "".join(ans_chars)
