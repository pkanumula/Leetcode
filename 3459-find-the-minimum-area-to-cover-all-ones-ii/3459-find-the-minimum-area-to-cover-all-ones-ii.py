from typing import List

class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        ones = [(i, j) for i in range(n) for j in range(m) if grid[i][j] == 1]

        def rect_area(cells):
            if not cells: return 0
            rmin = min(r for r, _ in cells)
            rmax = max(r for r, _ in cells)
            cmin = min(c for _, c in cells)
            cmax = max(c for _, c in cells)
            return (rmax - rmin + 1) * (cmax - cmin + 1)

        best = float('inf')

        # --- Case 1: vertical strips ---
        for c1 in range(m):
            for c2 in range(c1+1, m):
                g1 = [(r,c) for r,c in ones if c <= c1]
                g2 = [(r,c) for r,c in ones if c1 < c <= c2]
                g3 = [(r,c) for r,c in ones if c > c2]
                if not g1 or not g2 or not g3: continue
                best = min(best, rect_area(g1)+rect_area(g2)+rect_area(g3))

        # --- Case 2: horizontal strips ---
        for r1 in range(n):
            for r2 in range(r1+1, n):
                g1 = [(r,c) for r,c in ones if r <= r1]
                g2 = [(r,c) for r,c in ones if r1 < r <= r2]
                g3 = [(r,c) for r,c in ones if r > r2]
                if not g1 or not g2 or not g3: continue
                best = min(best, rect_area(g1)+rect_area(g2)+rect_area(g3))

        # --- Case 3: L-shaped partitions (split into 4 quadrants) ---
        for rcut in range(n-1):
            for ccut in range(m-1):
                q1 = [(r,c) for r,c in ones if r <= rcut and c <= ccut]
                q2 = [(r,c) for r,c in ones if r <= rcut and c > ccut]
                q3 = [(r,c) for r,c in ones if r > rcut and c <= ccut]
                q4 = [(r,c) for r,c in ones if r > rcut and c > ccut]
                quads = [q1,q2,q3,q4]
                for i in range(4):
                    for j in range(i+1,4):
                        g1 = quads[i]+quads[j]
                        g2 = quads[[0,1,2,3][0]]
                        g3 = quads[[0,1,2,3][1]]
                        # Actually simpler: check all ways to merge 2 quads into one group, remaining 2 are separate
                        remain = [k for k in range(4) if k not in (i,j)]
                        g2 = quads[remain[0]]
                        g3 = quads[remain[1]]
                        if not g1 or not g2 or not g3: continue
                        best = min(best, rect_area(g1)+rect_area(g2)+rect_area(g3))

        return best
