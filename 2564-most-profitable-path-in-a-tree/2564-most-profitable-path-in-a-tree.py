class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        import collections, sys
        sys.setrecursionlimit(10**6)
        n = len(amount)
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        parent = [-1] * n
        def build(u: int, par: int) -> None:
            parent[u] = par
            for v in graph[u]:
                if v == par: continue
                build(v, u)
        build(0, -1)
        
        INF = float('inf')
        bobTime = [INF] * n
        t, cur = 0, bob
        while cur != -1:
            bobTime[cur] = t
            t += 1
            cur = parent[cur]
            
        best = -10**9
        def dfs(u: int, time: int, curIncome: int, par: int) -> None:
            nonlocal best
            # Alice's income update based on arrival time compared to Bob's.
            if time < bobTime[u]:
                curIncome += amount[u]
            elif time == bobTime[u]:
                curIncome += amount[u] // 2
            # Leaf check: if not root and only one neighbor.
            if u and len(graph[u]) == 1:
                best = max(best, curIncome)
            for v in graph[u]:
                if v == par: continue
                dfs(v, time + 1, curIncome, u)
        dfs(0, 0, 0, -1)
        return best
