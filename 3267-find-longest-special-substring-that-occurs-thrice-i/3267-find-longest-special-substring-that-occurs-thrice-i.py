from collections import defaultdict

class Solution:
    def maximumLength(self, s: str) -> int:
        n = len(s)
        max_length = -1
        
        for length in range(1, n + 1):
            substring_count = defaultdict(int)
            for i in range(n - length + 1):
                substring = s[i:i+length]
                if len(set(substring)) == 1:  # Check if the substring is special
                    substring_count[substring] += 1
            
            for count in substring_count.values():
                if count >= 3:
                    max_length = max(max_length, length)
        
        return max_length