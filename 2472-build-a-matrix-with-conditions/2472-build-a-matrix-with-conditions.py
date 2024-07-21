from collections import defaultdict, deque

class Solution(object):
    def buildMatrix(self, k, rowConditions, colConditions):
        """
        :type k: int
        :type rowConditions: List[List[int]]
        :type colConditions: List[List[int]]
        :rtype: List[List[int]]
        """
        
        def topological_sort(conditions, k):
            in_degree = [0] * k
            graph = defaultdict(list)
            for u, v in conditions:
                graph[u-1].append(v-1)
                in_degree[v-1] += 1
            
            queue = deque([i for i in range(k) if in_degree[i] == 0])
            order = []
            
            while queue:
                node = queue.popleft()
                order.append(node)
                for neighbor in graph[node]:
                    in_degree[neighbor] -= 1
                    if in_degree[neighbor] == 0:
                        queue.append(neighbor)
            
            if len(order) == k:
                return order
            else:
                return []
        
        row_order = topological_sort(rowConditions, k)
        col_order = topological_sort(colConditions, k)
        
        if not row_order or not col_order:
            return []
        
        pos = [[0, 0] for _ in range(k)]
        for r, num in enumerate(row_order):
            pos[num][0] = r
        for c, num in enumerate(col_order):
            pos[num][1] = c
        
        matrix = [[0] * k for _ in range(k)]
        for num in range(k):
            r, c = pos[num]
            matrix[r][c] = num + 1
        
        return matrix