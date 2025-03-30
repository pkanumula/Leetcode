class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index = {char: i for i, char in enumerate(s)}
        start, end = 0, 0
        result = []
        
        for i, char in enumerate(s):
            end = max(end, last_index[char])
            if i == end:
                result.append(i - start + 1)
                start = i + 1
        
        return result
