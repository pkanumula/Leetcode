from collections import deque, defaultdict
from typing import List

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        graph = [[] for _ in range(n)]
        indegree = [0] * n
        
        # Build the graph and indegree array
        for u, v in edges:
            graph[u].append(v)
            indegree[v] += 1
        
        # Count of each color at each node (26 colors max)
        color_count = [[0] * 26 for _ in range(n)]
        queue = deque()
        
        # Initialize queue with nodes having zero indegree
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
        
        visited = 0
        max_color_value = 0
        
        while queue:
            node = queue.popleft()
            visited += 1
            color_index = ord(colors[node]) - ord('a')
            # Increment the color count for this node's own color
            color_count[node][color_index] += 1
            # Update the max color value seen so far
            max_color_value = max(max_color_value, color_count[node][color_index])
            
            for neighbor in graph[node]:
                for c in range(26):
                    color_count[neighbor][c] = max(
                        color_count[neighbor][c], color_count[node][c]
                    )
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        # If not all nodes were visited, there is a cycle
        return max_color_value if visited == n else -1
