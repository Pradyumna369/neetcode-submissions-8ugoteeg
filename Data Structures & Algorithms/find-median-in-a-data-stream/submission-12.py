class MedianFinder:

    def __init__(self):
        self.small = [] # Max heap
        self.large = [] # Min heap
        self.count = 0

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1 * num)
        if (self.small and self.large and -self.small[0] > self.large[0]):
            heapq.heappush(self.large, -heapq.heappop(self.small))
        if len(self.small) > len(self.large) + 1:
            heapq.heappush(self.large, -heapq.heappop(self.small))
        if len(self.large) > len(self.small) + 1:
            heapq.heappush(self.small, -heapq.heappop(self.large)) 

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]
        return (-self.small[0] + self.large[0]) / 2

            





        
        