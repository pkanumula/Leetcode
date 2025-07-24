from typing import List
import sys
sys.setrecursionlimit(10**7)

class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        n = len(nums)
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        subtreeXOR = [0] * n
        parent = [-1] * n
        
        # DFS to compute subtreeXOR and parent array
        def dfs(node, par):
            xor_sum = nums[node]
            parent[node] = par
            for nei in graph[node]:
                if nei == par:
                    continue
                xor_sum ^= dfs(nei, node)
            subtreeXOR[node] = xor_sum
            return xor_sum
        
        totalXOR = dfs(0, -1)
        
        # To check ancestor-descendant, we use DFS order timings
        time = 0
        in_time = [0]*n
        out_time = [0]*n
        
        def dfs_time(node, par):
            nonlocal time
            in_time[node] = time
            time += 1
            for nei in graph[node]:
                if nei == par:
                    continue
                dfs_time(nei, node)
            out_time[node] = time
            time += 1
        
        dfs_time(0, -1)
        
        def is_ancestor(u, v):
            # True if u is ancestor of v in rooted tree
            return in_time[u] <= in_time[v] and out_time[v] <= out_time[u]
        
        min_score = float('inf')
        
        # Consider all pairs of edges (represented by child nodes since each edge connects a node to its parent)
        # We'll consider all pairs of nodes except root since edges connect to parents.
        # Each edge corresponds to the subtree rooted at the child node.
        for i in range(1, n):
            for j in range(i+1, n):
                x = subtreeXOR[i]
                y = subtreeXOR[j]
                if is_ancestor(i, j):
                    # i ancestor of j
                    # Components:
                    # 1. subtree at j: y
                    # 2. subtree at i without j: x ^ y
                    # 3. rest: totalXOR ^ x
                    comp = [y, x ^ y, totalXOR ^ x]
                elif is_ancestor(j, i):
                    # j ancestor of i
                    # Components:
                    # 1. subtree at i: x
                    # 2. subtree at j without i: y ^ x
                    # 3. rest: totalXOR ^ y
                    comp = [x, y ^ x, totalXOR ^ y]
                else:
                    # Independent subtrees
                    # Components:
                    # 1. subtree i: x
                    # 2. subtree j: y
                    # 3. rest: totalXOR ^ x ^ y
                    comp = [x, y, totalXOR ^ x ^ y]
                
                score = max(comp) - min(comp)
                if score < min_score:
                    min_score = score
        
        return min_score
