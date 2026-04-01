"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda interval:(interval.start))
        previous = 0
        for interval in intervals:
            if interval.start < previous:
                return False
            else:
                previous = interval.end
        return True  