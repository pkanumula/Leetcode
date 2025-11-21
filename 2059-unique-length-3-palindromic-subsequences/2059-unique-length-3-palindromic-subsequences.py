class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        n = len(s)
        
        # First and last positions for each character 'a'..'z'
        first = [n] * 26
        last = [-1] * 26
        
        for i, ch in enumerate(s):
            idx = ord(ch) - ord('a')
            first[idx] = min(first[idx], i)
            last[idx] = max(last[idx], i)
        
        ans = 0
        
        # For each possible outer character
        for c in range(26):
            l = first[c]
            r = last[c]
            if l < r:  # needs at least two occurrences
                seen_middle = [False] * 26
                # Look at all chars between first and last occurrence
                for j in range(l + 1, r):
                    mid_idx = ord(s[j]) - ord('a')
                    seen_middle[mid_idx] = True
                
                ans += sum(seen_middle)
        
        return ans
