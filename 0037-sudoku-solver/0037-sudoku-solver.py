from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Bit helpers
        ALL = (1 << 9) - 1  # 0b1_1111_1111 -> digits 1..9 available
        
        def box_id(r: int, c: int) -> int:
            return (r // 3) * 3 + (c // 3)
        
        # Track used digits per row/col/box as bitmasks
        row_used = [0] * 9
        col_used = [0] * 9
        box_used = [0] * 9
        
        empties = []
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    empties.append((r, c))
                else:
                    d = ord(board[r][c]) - ord('1')  # 0..8
                    bit = 1 << d
                    row_used[r] |= bit
                    col_used[c] |= bit
                    box_used[box_id(r, c)] |= bit
        
        # Precompute candidate mask for a cell
        def candidates_mask(r: int, c: int) -> int:
            used = row_used[r] | col_used[c] | box_used[box_id(r, c)]
            return (~used) & ALL
        
        # Choose the empty cell with fewest candidates (MRV)
        def select_index() -> int:
            best_i = -1
            best_count = 10
            for i, (r, c) in enumerate(empties):
                if board[r][c] != '.':
                    continue
                m = candidates_mask(r, c)
                cnt = m.bit_count()
                if cnt < best_count:
                    best_count = cnt
                    best_i = i
                    if cnt == 1:
                        break
            return best_i
        
        def dfs() -> bool:
            idx = select_index()
            if idx == -1:
                return True  # solved
            
            r, c = empties[idx]
            m = candidates_mask(r, c)
            if m == 0:
                return False
            
            # Try each candidate digit
            while m:
                bit = m & -m
                m -= bit
                d = (bit.bit_length() - 1)  # 0..8
                ch = chr(ord('1') + d)
                
                # place
                board[r][c] = ch
                row_used[r] |= bit
                col_used[c] |= bit
                b = box_id(r, c)
                box_used[b] |= bit
                
                if dfs():
                    return True
                
                # undo
                board[r][c] = '.'
                row_used[r] ^= bit
                col_used[c] ^= bit
                box_used[b] ^= bit
            
            return False
        
        dfs()
