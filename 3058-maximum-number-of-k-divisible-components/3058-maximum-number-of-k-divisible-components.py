from collections import defaultdict
from typing import List

class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        def dfs(node, parent):
            total_sum = values[node]  # Initialize the sum of the current component
            for neighbor in tree[node]:
                if neighbor != parent:  # Avoid revisiting the parent node
                    child_sum = dfs(neighbor, node)
                    if child_sum % k == 0:
                        nonlocal components
                        components += 1  # Create a new component
                    else:
                        total_sum += child_sum
            return total_sum

        # Build the tree as an adjacency list
        tree = defaultdict(list)
        for a, b in edges:
            tree[a].append(b)
            tree[b].append(a)

        components = 0
        dfs(0, -1)
        return components + 1  # Add 1 for the root component
