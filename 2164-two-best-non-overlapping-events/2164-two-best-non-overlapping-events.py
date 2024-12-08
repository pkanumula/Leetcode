from typing import List
import bisect

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        # Sort events by end time
        events.sort(key=lambda x: x[1])
        
        # Create a list to store the max value up to each event
        max_values = [0] * len(events)
        max_value = 0
        
        for i in range(len(events)):
            max_value = max(max_value, events[i][2])
            max_values[i] = max_value
        
        result = 0
        
        # Sort events by their end time to facilitate binary search
        event_ends = [event[1] for event in events]
        
        for start, end, value in events:
            # Find the last event that ends before the current event's start time
            idx = bisect.bisect_right(event_ends, start - 1) - 1
            
            # Compute the maximum value with and without this event
            result = max(result, value + (max_values[idx] if idx >= 0 else 0))
        
        return result
