from heapq import heappop, heappush
from collections import defaultdict, deque

class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: list[list[int]]) -> list[int]:
        def dijkstra():
            dist = [float('inf')] * n
            dist[0] = 0
            pq = [(0, 0)]  # (distance, city)
            while pq:
                d, u = heappop(pq)
                if d > dist[u]:
                    continue
                for v in graph[u]:
                    if dist[u] + 1 < dist[v]:
                        dist[v] = dist[u] + 1
                        heappush(pq, (dist[v], v))
            return dist[n - 1]
        
        # Initialize the graph with the default roads
        graph = defaultdict(list)
        for i in range(n - 1):
            graph[i].append(i + 1)
        
        result = []
        for u, v in queries:
            graph[u].append(v)
            result.append(dijkstra())
        
        return result
