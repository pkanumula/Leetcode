import heapq
from collections import defaultdict

class Solution(object):
    def maxProbability(self, n, edges, succProb, start, end):
        """
        :type n: int
        :type edges: List[List[int]]
        :type succProb: List[float]
        :type start: int
        :type end: int
        :rtype: float
        """
        # Build the graph as an adjacency list
        graph = defaultdict(list)
        for (u, v), prob in zip(edges, succProb):
            graph[u].append((v, prob))
            graph[v].append((u, prob))
        
        # Max-heap to store the max probability to reach each node
        max_heap = [(-1.0, start)]  # (negative probability, node)
        max_prob = [0.0] * n  # Stores the max probability to reach each node
        max_prob[start] = 1.0
        
        while max_heap:
            prob, node = heapq.heappop(max_heap)
            prob = -prob  # Convert back to positive probability
            
            # If we reached the end node, return the probability
            if node == end:
                return prob
            
            # Traverse neighbors
            for neighbor, edge_prob in graph[node]:
                new_prob = prob * edge_prob
                if new_prob > max_prob[neighbor]:
                    max_prob[neighbor] = new_prob
                    heapq.heappush(max_heap, (-new_prob, neighbor))
        
        # If the end node is not reachable, return 0
        return 0.0
