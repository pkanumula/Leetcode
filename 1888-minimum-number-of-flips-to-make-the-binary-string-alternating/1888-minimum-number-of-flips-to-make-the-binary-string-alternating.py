class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        doubled = s + s
        
        # Count mismatches against pattern starting with '0': 010101...
        # and pattern starting with '1': 101010...
        mismatch_a = 0  # vs "010101..."
        mismatch_b = 0  # vs "101010..."
        
        result = float('inf')
        
        for i in range(2 * n):
            c = doubled[i]
            # Expected characters at position i
            expected_a = '0' if i % 2 == 0 else '1'  # pattern "0101..."
            expected_b = '1' if i % 2 == 0 else '0'  # pattern "1010..."
            
            # Add new character to window
            if c != expected_a:
                mismatch_a += 1
            if c != expected_b:
                mismatch_b += 1
            
            # Window has grown to size > n, remove leftmost character
            if i >= n:
                left = i - n
                left_c = doubled[left]
                expected_a_left = '0' if left % 2 == 0 else '1'
                expected_b_left = '1' if left % 2 == 0 else '0'
                
                if left_c != expected_a_left:
                    mismatch_a -= 1
                if left_c != expected_b_left:
                    mismatch_b -= 1
            
            # Once window is exactly size n, record result
            if i >= n - 1:
                result = min(result, mismatch_a, mismatch_b)
        
        return result