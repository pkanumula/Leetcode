from collections import deque, defaultdict
from typing import List

class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        def bfs_parity_counts(n, edges):
            # Build adjacency
            g = [[] for _ in range(n)]
            for u, v in edges:
                g[u].append(v)
                g[v].append(u)
            # BFS from 0, compute dist%2 and counts
            dist = [-1]*n
            q = deque([0])
            dist[0] = 0
            cnt_even = 1  # node 0
            cnt_odd = 0
            while q:
                u = q.popleft()
                for w in g[u]:
                    if dist[w] == -1:
                        dist[w] = dist[u] + 1
                        if dist[w] & 1:
                            cnt_odd += 1
                        else:
                            cnt_even += 1
                        q.append(w)
            return dist, cnt_even, cnt_odd

        # 1) Parities in tree1 from node 0
        dist1, e1, o1 = bfs_parity_counts(len(edges1)+1, edges1)
        # 2) Parities in tree2 from node 0 → we only need max(#even, #odd)
        _, e2, o2 = bfs_parity_counts(len(edges2)+1, edges2)
        best2 = max(e2, o2)

        # 3) For each i in tree1:
        #    if dist1[i] is even, E1_i = e1, else E1_i = o1
        #    answer[i] = E1_i + best2
        n = len(dist1)
        ans = [0]*n
        for i in range(n):
            ans[i] = (e1 if (dist1[i] % 2 == 0) else o1) + best2

        return ans
