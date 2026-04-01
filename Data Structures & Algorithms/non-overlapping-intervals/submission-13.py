class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[0])
        num = 0
        l = len(intervals)
        prevEnd = intervals[0][1]
        # longerInd = 0
        i = 1
        while i < l:
            if prevEnd > intervals[i][0]:
                # if intervals[i][1] >= prevEnd:
                #     num += 1
                #     prevEnd = min(prevEnd, )

                # else:
                #     intervals.pop(longerInd)
                #     longerEnd = intervals[i][1]
                #     longerInd = i
                num += 1
                prevEnd = min(prevEnd, intervals[i][1])
            else:
                prevEnd = intervals[i][1]
            i += 1
        return num