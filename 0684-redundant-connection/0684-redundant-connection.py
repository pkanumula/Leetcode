class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        parent = list(range(len(edges) + 1))
        rank = [0] * (len(edges) + 1)

        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])  # Path compression
            return parent[node]

        def union(node1, node2):
            root1 = find(node1)
            root2 = find(node2)

            if root1 == root2:
                return False
            if rank[root1] > rank[root2]:
                parent[root2] = root1
            elif rank[root1] < rank[root2]:
                parent[root1] = root2
            else:
                parent[root2] = root1
                rank[root1] += 1
            return True

        for a, b in edges:
            if not union(a, b):
                return [a, b]