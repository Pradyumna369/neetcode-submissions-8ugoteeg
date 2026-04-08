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

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.TimeMap:
            return ""
        
        values = self.TimeMap[key]
        l, r = 0, len(values) - 1

        if timestamp > values[r][1]:
            return values[r][0]

        l, r = 0, len(values) - 1
        while l < r:
            mid = (l + r + 1) // 2
            curr = values[mid][1]
            if timestamp >= curr:
                l = mid
            else:
                r = mid - 1
        if l == 0 and values[l][1] > timestamp:
            return ""
        return values[l][0] 
        

        
        
