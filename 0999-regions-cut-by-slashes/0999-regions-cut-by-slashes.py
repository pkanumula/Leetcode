class Solution(object):
    def regionsBySlashes(self, grid):
        n = len(grid)
        parent = list(range(4 * n * n))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                parent[rootY] = rootX

        for i in range(n):
            for j in range(n):
                root = 4 * (i * n + j)
                if grid[i][j] == '/':
                    union(root + 0, root + 3)
                    union(root + 1, root + 2)
                elif grid[i][j] == '\\':
                    union(root + 0, root + 1)
                    union(root + 2, root + 3)
                else:
                    union(root + 0, root + 1)
                    union(root + 1, root + 2)
                    union(root + 2, root + 3)
                
                # Union with the right cell
                if j + 1 < n:
                    union(root + 1, 4 * (i * n + (j + 1)) + 3)
                
                # Union with the bottom cell
                if i + 1 < n:
                    union(root + 2, 4 * ((i + 1) * n + j) + 0)

        return sum(find(x) == x for x in range(4 * n * n))