class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        answer = [0] * n
        
        # First pass: calculate operations moving from left to right
        count = 0  # Number of balls seen so far
        ops = 0    # Total operations so far
        for i in range(n):
            answer[i] += ops
            if boxes[i] == '1':
                count += 1
            ops += count
        
        # Second pass: calculate operations moving from right to left
        count = 0
        ops = 0
        for i in range(n - 1, -1, -1):
            answer[i] += ops
            if boxes[i] == '1':
                count += 1
            ops += count
        
        return answer
