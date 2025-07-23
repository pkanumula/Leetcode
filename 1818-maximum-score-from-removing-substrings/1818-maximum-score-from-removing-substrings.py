class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def remove_pair(s, first, second, val):
            stack = []
            score = 0
            for c in s:
                if stack and stack[-1] == first and c == second:
                    stack.pop()
                    score += val
                else:
                    stack.append(c)
            return "".join(stack), score
        
        total = 0
        # Remove higher value pair first
        if x > y:
            s, gain = remove_pair(s, 'a', 'b', x)
            total += gain
            s, gain = remove_pair(s, 'b', 'a', y)
            total += gain
        else:
            s, gain = remove_pair(s, 'b', 'a', y)
            total += gain
            s, gain = remove_pair(s, 'a', 'b', x)
            total += gain
        
        return total
