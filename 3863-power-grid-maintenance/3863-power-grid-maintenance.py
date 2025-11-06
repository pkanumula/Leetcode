from typing import List
import heapq

class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        # --- DSU (Union-Find) ---
        parent = list(range(c + 1))
        size = [1] * (c + 1)

        def find(a: int) -> int:
            while parent[a] != a:
                parent[a] = parent[parent[a]]
                a = parent[a]
            return a

        def union(a: int, b: int) -> None:
            ra, rb = find(a), find(b)
            if ra == rb: 
                return
            if size[ra] < size[rb]:
                ra, rb = rb, ra
            parent[rb] = ra
            size[ra] += size[rb]

        for u, v in connections:
            union(u, v)

        # Group nodes by component root
        members = [[] for _ in range(c + 1)]
        for node in range(1, c + 1):
            members[find(node)].append(node)

        # Min-heap per component
        heaps = [None] * (c + 1)
        for r in range(1, c + 1):
            if members[r]:
                heap = members[r][:]
                heapq.heapify(heap)
                heaps[r] = heap
            else:
                heaps[r] = []

        # Online status
        online = [False] * (c + 1)
        for i in range(1, c + 1):
            online[i] = True

        # Helper to get smallest online in component of x
        def smallest_online_in_comp(x: int) -> int:
            r = find(x)
            heap = heaps[r]
            while heap and not online[heap[0]]:
                heapq.heappop(heap)
            return heap[0] if heap else -1

        # Process queries
        ans = []
        for t, x in queries:
            if t == 1:
                if online[x]:
                    ans.append(x)
                else:
                    ans.append(smallest_online_in_comp(x))
            else:  # t == 2
                online[x] = False

        return ans
