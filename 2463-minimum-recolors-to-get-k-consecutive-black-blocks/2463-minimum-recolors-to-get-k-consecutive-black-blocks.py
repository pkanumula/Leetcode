class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        min_operations = operations = blocks[:k].count('W')
        
        for i in range(k, len(blocks)):
            operations += blocks[i] == 'W'
            operations -= blocks[i - k] == 'W'
            min_operations = min(min_operations, operations)

        return min_operations
