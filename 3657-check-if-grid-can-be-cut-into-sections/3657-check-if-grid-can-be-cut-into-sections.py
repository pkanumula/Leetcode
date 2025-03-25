class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        def can_cut(axis):
            rects = []
            for r in rectangles:
                if axis == 'x':
                    rects.append((r[0], r[2]))  # x1, x2
                else:
                    rects.append((r[1], r[3]))  # y1, y2
            rects.sort()
            parts = []
            curr_end = -1
            for start, end in rects:
                if start >= curr_end:
                    parts.append((start, end))
                    curr_end = end
                else:
                    curr_end = max(curr_end, end)
                    parts[-1] = (parts[-1][0], curr_end)
            return len(parts) >= 3
        
        return can_cut('x') or can_cut('y')
