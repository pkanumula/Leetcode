class MyCalendar(object):

    def __init__(self):
        self.calendar = []

    def book(self, start, end):
        for s, e in self.calendar:
            if start < e and end > s:  # Check for overlap
                return False
        self.calendar.append((start, end))
        return True
