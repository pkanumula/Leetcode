class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        if rows == 1 or not encodedText:
            return encodedText
        
        n = len(encodedText)
        cols = n // rows
        result = []
        
        for c in range(cols):
            r = 0
            while r < rows and (c + r) < cols:
                result.append(encodedText[r * cols + c + r])
                r += 1
        
        return ''.join(result).rstrip(' ')