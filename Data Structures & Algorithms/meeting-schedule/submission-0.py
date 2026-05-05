class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)  # Use .start, not [0]
        
        for i in range(1, len(intervals)):
            previous_end = intervals[i - 1].end    # Use .end, not [1]
            current_start = intervals[i].start     # Use .start, not [0]
            
            if current_start < previous_end:       # Conflict found
                return False
        
        return True