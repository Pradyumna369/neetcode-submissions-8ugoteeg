class TimeMap:
    '''
    TimeMap = {
        "key" : [["happy", 1], ["sad", 3]]
        timeMap.get("alice", 3) -> "sad"
        timeMap.get("alice", 4) -> "sad"
    }
    '''

    def __init__(self):
        self.TimeMap = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.TimeMap:
            self.TimeMap[key] = [[value, timestamp]]
        else:
            self.TimeMap[key].append([value, timestamp])

    def get(self, key, timestamp):
        if key not in self.TimeMap:
            return ""
        res = ""
        values = self.TimeMap[key]
        # l, r = 0, len(values) - 1
        # while l <= r:
        #     m = (l + r) // 2
        #     # perform binary search to find the rightmost timestamp t <= timestamp. tracking the best candidate
        #     # in res as i go
        #     if values[m][1] <= timestamp:
        #         res = values[m][0]
        #         l = m + 1
        #     else:
        #         r = m - 1
        # return res
        l, r = 0, len(values)  # r = len for true insertion point
        while l < r:
            mid = (l + r) // 2
            if timestamp < values[mid][1]:
                r = mid
            else:
                l = mid + 1
        if l == 0:
            return ""
        return values[l - 1][0]
        
         
