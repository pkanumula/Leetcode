from collections import Counter
from typing import List

class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        # 1) Build the trie
        root = {}
        for path in paths:
            node = root
            for folder in path:
                node = node.setdefault(folder, {})

        # 2) Serialize subtrees (only for non‐leaf nodes) and count frequencies
        code = {}  # maps id(node) -> its serialization
        def encode(node):
            # If leaf, return empty string (and do NOT record in code)
            if not node:
                return ""
            # Otherwise, serialize children in sorted order
            parts = []
            for name in sorted(node):
                parts.append(f"({name},{encode(node[name])})")
            serial = "".join(parts)
            code[id(node)] = serial
            return serial

        encode(root)
        freq = Counter(code.values())

        # 3) DFS to collect remaining paths, skipping only true duplicates
        ans = []
        def dfs(node, path):
            sid = code.get(id(node))
            # If this node has a serialization and it’s duplicated, skip entire subtree
            if sid is not None and freq[sid] > 1:
                return

            # Record this folder (except the imaginary root at path==[])
            if path:
                ans.append(path.copy())

            for name in sorted(node):
                path.append(name)
                dfs(node[name], path)
                path.pop()

        dfs(root, [])
        return ans
