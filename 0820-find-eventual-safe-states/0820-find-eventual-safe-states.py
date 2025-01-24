from collections import deque, defaultdict

class Solution:
    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
        n = len(graph)
        reverse_graph = defaultdict(list)
        in_degree = [0] * n

        # Build reverse graph and calculate in-degree
        for node, neighbors in enumerate(graph):
            for neighbor in neighbors:
                reverse_graph[neighbor].append(node)
            in_degree[node] = len(neighbors)

        # Start with nodes having in-degree 0 (terminal nodes)
        queue = deque([node for node in range(n) if in_degree[node] == 0])
        safe_nodes = []

        while queue:
            node = queue.popleft()
            safe_nodes.append(node)
            for neighbor in reverse_graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # Return sorted list of safe nodes
        return sorted(safe_nodes)
