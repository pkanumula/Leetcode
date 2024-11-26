from collections import defaultdict, deque

class Solution:
    def findChampion(self, n: int, edges: list[list[int]]) -> int:
        # Build the graph and in-degree array
        graph = defaultdict(list)
        in_degree = [0] * n
        
        for u, v in edges:
            graph[u].append(v)
            in_degree[v] += 1
        
        # Find all nodes with 0 in-degree
        zero_in_degree = deque([i for i in range(n) if in_degree[i] == 0])
        
        # If there is not exactly one node with 0 in-degree, return -1
        if len(zero_in_degree) != 1:
            return -1
        
        # Perform topological sort and check if only one node is reachable
        champion = zero_in_degree[0]
        visited_count = 0
        
        while zero_in_degree:
            node = zero_in_degree.popleft()
            visited_count += 1
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    zero_in_degree.append(neighbor)
        
        # If not all nodes are reachable or there are cycles, return -1
        return champion if visited_count == n else -1
