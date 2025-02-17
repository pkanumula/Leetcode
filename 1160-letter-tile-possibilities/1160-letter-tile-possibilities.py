from itertools import permutations

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        unique_sequences = set()
        for i in range(1, len(tiles) + 1):
            unique_sequences.update(set(permutations(tiles, i)))
        return len(unique_sequences)
