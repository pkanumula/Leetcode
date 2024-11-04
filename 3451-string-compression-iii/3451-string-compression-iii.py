class Solution:
    def compressedString(self, word: str) -> str:
        comp = []
        i = 0
        n = len(word)
        
        while i < n:
            count = 1
            while i + 1 < n and word[i] == word[i + 1] and count < 9:
                count += 1
                i += 1
            
            comp.append(f"{count}{word[i]}")
            i += 1
        
        return ''.join(comp)