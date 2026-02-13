class Solution:
    def longestBalanced(self, s: str) -> int:
        # We try all non-empty subsets of {'a','b','c'} as the set of
        # characters that are present in a balanced substring.
        # There are only 7 such subsets -> constant factor.
        
        def longest_for_mask(mask: int) -> int:
            included = [i for i in range(3) if (mask >> i) & 1]      # chars that must have equal counts
            excluded = [i for i in range(3) if not ((mask >> i) & 1)] # chars that must have count 0
            
            base = included[0]   # reference included char for differences
            cnt = [0, 0, 0]      # prefix counts of a,b,c
            
            def make_key() -> tuple:
                # Conditions encoded in key:
                # 1) included chars all equal <=> prefix differences to base are equal
                # 2) excluded chars absent <=> excluded prefix counts unchanged
                key = []
                for ch in included[1:]:
                    key.append(cnt[ch] - cnt[base])
                for ch in excluded:
                    key.append(cnt[ch])
                return tuple(key)
            
            first_pos = {make_key(): 0}  # earliest prefix index for each key
            best = 0
            
            for i, ch in enumerate(s, 1):  # prefix index i (1-based over chars)
                cnt[ord(ch) - ord('a')] += 1
                key = make_key()
                
                if key in first_pos:
                    best = max(best, i - first_pos[key])
                else:
                    first_pos[key] = i
            
            return best
        
        ans = 0
        for mask in range(1, 8):  # 1..7 => all non-empty subsets
            ans = max(ans, longest_for_mask(mask))
        
        return ans
