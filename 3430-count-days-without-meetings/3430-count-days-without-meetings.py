class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        # Sort meetings by start time
        meetings.sort()

        merged = []
        for start, end in meetings:
            if not merged or merged[-1][1] < start - 1:
                merged.append([start, end])
            else:
                merged[-1][1] = max(merged[-1][1], end)

        # Calculate total days covered by meetings
        meeting_days = sum(end - start + 1 for start, end in merged)

        return days - meeting_days
