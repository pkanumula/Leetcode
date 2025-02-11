class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        part_len = len(part)

        for char in s:
            stack.append(char)
            # Check if the last characters in the stack match the 'part'
            if ''.join(stack[-part_len:]) == part:
                # Remove the last 'part_len' characters from the stack
                del stack[-part_len:]
        
        return ''.join(stack)
