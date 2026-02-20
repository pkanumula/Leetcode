class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        # Base: smallest special strings can't be improved
        if len(s) <= 2:
            return s

        parts = []
        bal = 0
        start = 0

        # Split into consecutive top-level special substrings
        for i, ch in enumerate(s):
            bal += 1 if ch == '1' else -1
            if bal == 0:
                # s[start:i+1] is a special block: 1 + (inner) + 0
                inner = s[start + 1 : i]
                parts.append('1' + self.makeLargestSpecial(inner) + '0')
                start = i + 1

        # To maximize lexicographically, sort blocks descending and concatenate
        parts.sort(reverse=True)
        return ''.join(parts)
