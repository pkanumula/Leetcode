class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        import math, bisect
        
        n = len(s)
        # Positions of all zeros
        zero_pos = [i for i, c in enumerate(s) if c == '0']
        Z = len(zero_pos)
        
        # Max possible zeros in any valid substring: z^2 <= n -> z <= sqrt(n)
        B = int(math.isqrt(n))
        
        ans = 0
        
        for l in range(n):
            # Find first zero at or after l
            p = bisect.bisect_left(zero_pos, l)
            
            # If there is no zero from l onwards, all substrings starting at l are all ones
            if p == Z:
                ans += n - l
                continue
            
            first_zero = zero_pos[p]
            
            # Substrings starting at l with 0 zeros:
            # s[l..r] where r < first_zero
            if first_zero > l:
                ans += first_zero - l
            
            # Now handle substrings with k >= 1 zeros
            max_k = min(B, Z - p)  # can't use more zeros than we have after l
            for k in range(1, max_k + 1):
                # Position of k-th zero after l
                zk = zero_pos[p + k - 1]
                
                # Need length >= k^2 + k  ->  r - l + 1 >= k^2 + k
                needed_len = k * k + k
                r_min = max(zk, l + needed_len - 1)  # must include k-th zero and be long enough
                
                # r must be before the (k+1)-th zero (if it exists), otherwise zeros > k
                if p + k < Z:
                    next_zero = zero_pos[p + k]
                    r_max = next_zero - 1
                else:
                    r_max = n - 1  # no more zeros, can go to end
                
                if r_min <= r_max:
                    ans += (r_max - r_min + 1)
        
        return ans
