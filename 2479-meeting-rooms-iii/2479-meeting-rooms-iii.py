import heapq
from typing import List

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # sort by original start time
        meetings.sort(key=lambda x: x[0])
        
        # min-heap of free room indices
        free_rooms = list(range(n))
        heapq.heapify(free_rooms)
        
        # min-heap of (end_time, room_index) for busy rooms
        busy_rooms: List[tuple[int,int]] = []
        
        # count how many meetings each room held
        count = [0] * n
        
        for start, end in meetings:
            duration = end - start
            
            # free up any rooms that have completed by 'start'
            while busy_rooms and busy_rooms[0][0] <= start:
                freed_end, freed_room = heapq.heappop(busy_rooms)
                heapq.heappush(free_rooms, freed_room)
            
            if free_rooms:
                # assign the lowest-index free room immediately
                room = heapq.heappop(free_rooms)
                actual_start = start
            else:
                # wait for the earliest busy room to free up
                freed_end, room = heapq.heappop(busy_rooms)
                actual_start = freed_end
            
            # schedule this meeting in 'room'
            actual_end = actual_start + duration
            heapq.heappush(busy_rooms, (actual_end, room))
            count[room] += 1
        
        # return the room with the highest count (tie → lowest index)
        return min(
            range(n),
            key=lambda i: (-count[i], i)
        )
