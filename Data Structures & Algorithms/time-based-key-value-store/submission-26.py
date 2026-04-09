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
        values = self.TimeMap[key]
        l, r = 0, len(values)
        while l < r:
            mid = (l + r) // 2
            if timestamp < values[mid][1]:
                r = mid
            else:
                l = mid + 1
        if l == 0:
            if values[0][1] > timestamp:
                return ""
            else:
                return values[0][0]
        else:
            return values[l - 1][0]
         
