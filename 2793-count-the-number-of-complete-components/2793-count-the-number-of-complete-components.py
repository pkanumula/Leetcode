from collections import defaultdict

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n
        res = 0

        def dfs(node, nodes):
            visited[node] = True
            nodes.append(node)
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    dfs(neighbor, nodes)

        for i in range(n):
            if not visited[i]:
                nodes = []
                dfs(i, nodes)
                size = len(nodes)
                edge_count = sum(len(graph[node]) for node in nodes) // 2
                if edge_count == size * (size - 1) // 2:
                    res += 1

        return res
