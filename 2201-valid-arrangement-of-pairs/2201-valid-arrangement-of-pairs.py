from collections import defaultdict, deque

class Solution:
    def validArrangement(self, pairs: list[list[int]]) -> list[list[int]]:
        # Create graph and calculate in-degrees and out-degrees
        graph = defaultdict(list)
        in_degree = defaultdict(int)
        out_degree = defaultdict(int)
        
        for start, end in pairs:
            graph[start].append(end)
            out_degree[start] += 1
            in_degree[end] += 1

        # Find the starting node
        start_node = None
        for node in graph:
            if out_degree[node] > in_degree[node]:
                start_node = node
                break
        if start_node is None:
            start_node = pairs[0][0]

        # Hierholzer's algorithm for Eulerian path
        result = []
        stack = [start_node]
        while stack:
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop())
            result.append(stack.pop())

        # Reverse the result to get the correct order
        result.reverse()
        return [[result[i], result[i + 1]] for i in range(len(result) - 1)]
