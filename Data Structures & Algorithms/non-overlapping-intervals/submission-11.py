class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])

        num = 0
        prevEnd = intervals[0][1]

        for i in range(1, len(intervals)):
            if intervals[i][0] < prevEnd:   # overlap
                num += 1
                prevEnd = min(prevEnd, intervals[i][1])  # keep shorter interval
            else:
                prevEnd = intervals[i][1]

        return num