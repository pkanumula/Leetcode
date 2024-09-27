class MyCalendarTwo(object):

    def __init__(self):
        self.bookings = []
        self.overlaps = []

    def book(self, start, end):
        for os, oe in self.overlaps:
            if start < oe and end > os:  # Check for triple booking
                return False
        
        for bs, be in self.bookings:
            if start < be and end > bs:  # Check for double booking
                self.overlaps.append((max(start, bs), min(end, be)))
        
        self.bookings.append((start, end))
        return True
