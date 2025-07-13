from typing import List

class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        
        i = j = matches = 0
        n, m = len(players), len(trainers)
        
        while i < n and j < m:
            if trainers[j] >= players[i]:
                matches += 1
                i += 1
                j += 1
            else:
                j += 1
        
        return matches
