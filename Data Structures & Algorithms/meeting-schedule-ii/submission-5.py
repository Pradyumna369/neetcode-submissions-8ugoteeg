"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key = lambda interval:interval.start)
        num = 0
        myHeap = []

        for interval in intervals:
            while myHeap and interval.start >= myHeap[0]:
                heapq.heappop(myHeap)
            heapq.heappush(myHeap, interval.end)
            num = max(num, len(myHeap))
        return num