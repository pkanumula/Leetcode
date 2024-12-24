from collections import deque

class Solution:
    def minimumDiameterAfterMerge(self, edges1, edges2):
        def tree_diameter(edges, n):
            # Helper function to calculate tree diameter using BFS
            def bfs(farthest_node):
                visited = [-1] * n
                visited[farthest_node] = 0
                queue = deque([farthest_node])
                max_dist = 0
                farthest_point = farthest_node

                while queue:
                    node = queue.popleft()
                    for neighbor in adj[node]:
                        if visited[neighbor] == -1:
                            visited[neighbor] = visited[node] + 1
                            queue.append(neighbor)
                            if visited[neighbor] > max_dist:
                                max_dist = visited[neighbor]
                                farthest_point = neighbor

                return farthest_point, max_dist

            adj = [[] for _ in range(n)]
            for u, v in edges:
                adj[u].append(v)
                adj[v].append(u)

            # First BFS to find the farthest point from an arbitrary node (node 0)
            farthest_point, _ = bfs(0)

            # Second BFS from the farthest point to determine the diameter
            _, diameter = bfs(farthest_point)

            return diameter

        # Number of nodes in both trees
        n1 = len(edges1) + 1
        n2 = len(edges2) + 1

        # Calculate diameters of both trees
        d1 = tree_diameter(edges1, n1)
        d2 = tree_diameter(edges2, n2)

        # The minimum diameter of the merged tree
        return max((d1 + 1) // 2 + (d2 + 1) // 2 + 1, max(d1, d2))
