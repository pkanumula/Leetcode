class Solution(object):
    def minGroups(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        # Create events for the start and end of each interval
        events = []
        for start, end in intervals:
            events.append((start, 1))   # 1 for interval starting
            events.append((end + 1, -1))  # -1 for interval ending

        # Sort the events by time
        events.sort()

        # Keep track of the maximum number of overlapping intervals
        current_groups = 0
        max_groups = 0

        # Process all events in order
        for time, event_type in events:
            current_groups += event_type
            max_groups = max(max_groups, current_groups)

        return max_groups
