class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        l = len(intervals)
        i = 1
        curr = intervals[0]
        res = []
        while i < l:
            if intervals[i][0] <= curr[1]:
                curr[1] = max(intervals[i][1], curr[1])
            else:
                res.append(curr)
                curr = intervals[i]
            i += 1
        res.append(curr)
        return res
            



        