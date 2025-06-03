from collections import deque
from typing import List

class Solution:
    def maxCandies(self, status: List[int], candies: List[int], 
                   keys: List[List[int]], containedBoxes: List[List[int]], 
                   initialBoxes: List[int]) -> int:
        # Total number of candies collected so far
        total_candies = 0
        
        # have_box: set of all boxes we currently possess (opened or not)
        have_box = set(initialBoxes)
        # have_key: set of box‐indices whose keys we have
        have_key = set(i for i, s in enumerate(status) if s == 1 and i in have_box)
        # opened: set of boxes we've already opened/processed
        opened = set()
        
        # We’ll repeatedly scan through have_box and open any box that is both:
        #   - not yet opened
        #   - unlocked (status == 1 or we have its key)
        #
        # As soon as we open a box, we collect candies, add its containedBoxes, add any new keys,
        # and mark it as opened. We keep looping until no more progress is possible.
        made_progress = True
        while made_progress:
            made_progress = False
            
            # Iterate over a snapshot of boxes we possess
            for b in list(have_box):
                # If already opened, skip
                if b in opened:
                    continue
                
                # If this box is locked and we don't have its key, skip for now
                if status[b] == 0 and b not in have_key:
                    continue
                
                # Otherwise, we can open it now:
                opened.add(b)
                made_progress = True
                total_candies += candies[b]
                
                # Collect any new keys from this box
                for k in keys[b]:
                    if k not in have_key:
                        have_key.add(k)
                
                # Collect any new boxes contained inside
                for nb in containedBoxes[b]:
                    if nb not in have_box:
                        have_box.add(nb)
            
            # Loop again if we opened at least one box in this pass
        
        return total_candies
