class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        # Helper function to convert "HH:MM" to total minutes
        def timeToMinutes(time):
            hours, minutes = map(int, time.split(":"))
            return hours * 60 + minutes
        
        # Convert all timePoints to minutes
        minutes_list = [timeToMinutes(time) for time in timePoints]
        
        # Sort the list of minutes
        minutes_list.sort()
        
        # Initialize minimum difference with a large number
        min_diff = float('inf')
        
        # Compute the minimum difference between consecutive times
        for i in range(1, len(minutes_list)):
            min_diff = min(min_diff, minutes_list[i] - minutes_list[i-1])
        
        # Don't forget to consider the circular difference between the first and last time points
        circular_diff = (1440 + minutes_list[0] - minutes_list[-1]) % 1440
        min_diff = min(min_diff, circular_diff)
        
        return min_diff
