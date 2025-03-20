from typing import List
from collections import defaultdict, deque

class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        # Graph representation
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        # Find connected components and their minimum AND cost
        component = [-1] * n
        min_and_cost = {}

        def bfs(start, comp_id):
            queue = deque([start])
            component[start] = comp_id
            and_value = -1  # Initialize to all bits set

            while queue:
                node = queue.popleft()
                for neighbor, weight in graph[node]:
                    and_value &= weight  # Apply AND operation
                    if component[neighbor] == -1:
                        component[neighbor] = comp_id
                        queue.append(neighbor)

            min_and_cost[comp_id] = and_value

        # Assign component IDs and calculate min AND value
        comp_id = 0
        for i in range(n):
            if component[i] == -1:
                bfs(i, comp_id)
                comp_id += 1

        # Process queries
        result = []
        for si, ti in query:
            if component[si] == component[ti]:  # Same component
                result.append(min_and_cost[component[si]])
            else:
                result.append(-1)  # No path exists

        return result
