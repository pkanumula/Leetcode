from collections import deque

class Solution:
    def secondMinimum(self, n, edges, time, change):
        # Build adjacency list
        graph = [[] for _ in range(n + 1)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # BFS
        queue = deque([(1, 0)])  # (node, time)
        times = [[] for _ in range(n + 1)]
        
        while queue:
            node, curr_time = queue.popleft()
            
            # If we've found two times for the last node, we can return the second one
            if node == n and len(times[n]) == 2:
                return times[n][1]
            
            # Calculate the actual arrival time considering traffic light
            if curr_time % (2 * change) >= change:
                curr_time = curr_time + (2 * change - curr_time % (2 * change))
            next_time = curr_time + time
            
            for neighbor in graph[node]:
                if len(times[neighbor]) < 2 and (not times[neighbor] or next_time > times[neighbor][-1]):
                    times[neighbor].append(next_time)
                    queue.append((neighbor, next_time))
        
        return -1  # Should never reach here given the problem constraints