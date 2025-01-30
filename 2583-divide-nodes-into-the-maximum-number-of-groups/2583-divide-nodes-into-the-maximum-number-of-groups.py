from collections import defaultdict, deque
from typing import List

class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        # Step 1: Build the graph
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        # Step 2: BFS to determine group distance
        def bfs_max_groups(start: int) -> int:
            queue = deque([(start, 1)])
            visited = {start: 1}
            max_level = 1

            while queue:
                node, level = queue.popleft()
                max_level = max(max_level, level)

                for neighbor in graph[node]:
                    if neighbor not in visited:
                        visited[neighbor] = level + 1
                        queue.append((neighbor, level + 1))
                    elif abs(visited[neighbor] - level) != 1:
                        return -1  # Invalid grouping condition

            return max_level

        # Step 3: Find connected components and calculate the maximum groups
        visited_components = set()
        total_groups = 0

        for node in range(1, n + 1):
            if node not in visited_components:
                # Find the nodes in the current component
                component_nodes = set()
                queue = deque([node])
                while queue:
                    current = queue.popleft()
                    if current in component_nodes:
                        continue
                    component_nodes.add(current)
                    visited_components.add(current)
                    for neighbor in graph[current]:
                        if neighbor not in visited_components:
                            queue.append(neighbor)

                # Check the maximum groups for this component
                max_groups = -1
                for comp_node in component_nodes:
                    result = bfs_max_groups(comp_node)
                    if result == -1:
                        return -1
                    max_groups = max(max_groups, result)

                total_groups += max_groups

        return total_groups
