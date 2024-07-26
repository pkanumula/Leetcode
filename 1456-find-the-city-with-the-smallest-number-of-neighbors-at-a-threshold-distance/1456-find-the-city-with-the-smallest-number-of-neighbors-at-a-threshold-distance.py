import heapq

class Solution(object):
    def findTheCity(self, n, edges, distanceThreshold):
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        def dijkstra(start):
            distances = [float('inf')] * n
            distances[start] = 0
            heap = [(0, start)]
            while heap:
                d, u = heapq.heappop(heap)
                if d > distances[u]:
                    continue
                for v, w in graph[u]:
                    if distances[u] + w < distances[v]:
                        distances[v] = distances[u] + w
                        heapq.heappush(heap, (distances[v], v))
            return [d for d in distances if d <= distanceThreshold]

        min_reachable = float('inf')
        max_city = -1
        for city in range(n):
            reachable = len(dijkstra(city))
            if reachable < min_reachable:
                min_reachable = reachable
                max_city = city
            elif reachable == min_reachable:
                max_city = max(max_city, city)

        return max_city