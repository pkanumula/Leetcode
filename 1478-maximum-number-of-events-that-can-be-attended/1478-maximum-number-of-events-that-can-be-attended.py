from typing import List
import heapq

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        # Sort events by their start day
        events.sort()
        total_days = max(end for _, end in events)
        event_index = 0
        attended = 0
        min_heap = []

        for day in range(1, total_days + 1):
            # Add all events starting today
            while event_index < len(events) and events[event_index][0] == day:
                heapq.heappush(min_heap, events[event_index][1])
                event_index += 1
            
            # Remove all events that have already expired
            while min_heap and min_heap[0] < day:
                heapq.heappop(min_heap)
            
            # Attend the event that ends the earliest
            if min_heap:
                heapq.heappop(min_heap)
                attended += 1
        
        return attended
