class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        
        for char in s:
            if char.isdigit():
                if stack:
                    stack.pop()  # Remove the closest non-digit character to its left
            else:
                stack.append(char)
        
        return ''.join(stack)