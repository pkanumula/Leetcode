from typing import List

class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Segment Tree Setup
        # Size needs to be a power of 2 for easy implementation
        size = 1
        while size < n:
            size *= 2
            
        # Trees store min and max to allow searching for 0
        mn = [0] * (2 * size)
        mx = [0] * (2 * size)
        lazy = [0] * (2 * size)
        
        # Helper to push lazy updates down to children
        def push(x):
            if lazy[x] != 0:
                lz = lazy[x]
                
                lazy[2*x] += lz
                mn[2*x] += lz
                mx[2*x] += lz
                
                lazy[2*x+1] += lz
                mn[2*x+1] += lz
                mx[2*x+1] += lz
                
                lazy[x] = 0
        
        # Range Update
        def update(l, r, val, x, lx, rx):
            if lx >= r or rx <= l:
                return
            if lx >= l and rx <= r:
                mn[x] += val
                mx[x] += val
                lazy[x] += val
                return
            
            push(x)
            mid = (lx + rx) // 2
            update(l, r, val, 2*x, lx, mid)
            update(l, r, val, 2*x+1, mid, rx)
            mn[x] = min(mn[2*x], mn[2*x+1])
            mx[x] = max(mx[2*x], mx[2*x+1])
            
        # Find the leftmost index L <= limit with value 0
        def find_first_zero(x, lx, rx, limit):
            # Optimization: If 0 is not within [min, max], it doesn't exist here
            if mn[x] > 0 or mx[x] < 0:
                return -1
            if lx >= limit:
                return -1
            if rx - lx == 1:
                return lx
            
            push(x)
            mid = (lx + rx) // 2
            
            # Try left child first (to find the longest subarray / smallest L)
            res = find_first_zero(2*x, lx, mid, limit)
            if res != -1:
                return res
            
            # Try right child
            return find_first_zero(2*x+1, mid, rx, limit)

        last_pos = {}
        max_len = 0
        
        for i, num in enumerate(nums):
            prev = last_pos.get(num, -1)
            
            # Even adds 1, Odd subtracts 1
            val = 1 if num % 2 == 0 else -1
            
            # Update the range of start indices valid for this new distinct number
            # Range: [prev + 1, i + 1) in 0-based indexing logic
            update(prev + 1, i + 1, val, 1, 0, size)
            
            last_pos[num] = i
            
            # Find smallest L such that value is 0
            l_idx = find_first_zero(1, 0, size, i + 1)
            
            if l_idx != -1:
                current_len = i - l_idx + 1
                if current_len > max_len:
                    max_len = current_len
                    
        return max_len