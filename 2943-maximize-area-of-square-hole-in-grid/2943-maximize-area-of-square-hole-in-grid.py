from typing import List

class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        
        def longest_consecutive_run(bars: List[int]) -> int:
            if not bars:
                return 1  # no removal -> side length = 1 cell
            
            bars.sort()
            best = 1
            cur = 1
            
            for i in range(1, len(bars)):
                if bars[i] == bars[i - 1] + 1:
                    cur += 1
                else:
                    cur = 1
                best = max(best, cur)
            
            return best + 1  # run length k -> merged cells = k + 1
        
        max_height = longest_consecutive_run(hBars)
        max_width = longest_consecutive_run(vBars)
        
        side = min(max_height, max_width)
        return side * side
