from collections import deque
from typing import List

class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        # Build adjacency lists
        n = max(u for e in edges1 for u in e) + 1
        m = max(u for e in edges2 for u in e) + 1
        g1 = [[] for _ in range(n)]
        g2 = [[] for _ in range(m)]
        for u, v in edges1:
            g1[u].append(v)
            g1[v].append(u)
        for u, v in edges2:
            g2[u].append(v)
            g2[v].append(u)
        
        def bfs_count(adj: List[List[int]], dist_limit: int) -> List[int]:
            """For each node x, return how many nodes are within dist_limit of x (inclusive)."""
            N = len(adj)
            count = [0]*N
            for src in range(N):
                seen = [False]*N
                dq = deque([(src,0)])
                seen[src] = True
                c = 0
                while dq:
                    u, d = dq.popleft()
                    if d > dist_limit:
                        continue
                    # u is within the limit
                    c += 1
                    for w in adj[u]:
                        if not seen[w]:
                            seen[w] = True
                            dq.append((w, d+1))
                count[src] = c
            return count
        
        # Count reachable within k in tree1
        count1 = bfs_count(g1, k)
        # Count reachable within k-1 in tree2 (via the new edge adds +1)
        # if k == 0, k-1 = -1 → count2 will be all zeros, as desired
        count2 = bfs_count(g2, k-1)
        best2 = max(count2)  # best choice of which node in tree2 to attach
        
        # For each i in tree1, best total = its own count + best2
        return [count1[i] + best2 for i in range(n)]
