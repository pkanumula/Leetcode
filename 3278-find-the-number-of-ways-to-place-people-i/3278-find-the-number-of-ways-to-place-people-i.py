class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        n = len(points)
        ans = 0
        
        for i in range(n):
            xi, yi = points[i]
            for j in range(n):
                if i == j:
                    continue
                xj, yj = points[j]
                
                # A (i) must be upper-left (allow shared row/column)
                if xi <= xj and yi >= yj:
                    # Check rectangle/line [xi..xj] x [yj..yi] is empty
                    empty = True
                    for k in range(n):
                        if k == i or k == j:
                            continue
                        xk, yk = points[k]
                        if xi <= xk <= xj and yj <= yk <= yi:
                            empty = False
                            break
                    if empty:
                        ans += 1
        return ans
