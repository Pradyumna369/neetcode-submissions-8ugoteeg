class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(point):
            x, y = point
            distance = x ** 2 + y ** 2
            return distance
        self.heap = []
        ans = []
        for point in points:
            dist = -distance(point)
            x, y = point
            heapq.heappush(self.heap, [dist, x, y])
            if len(self.heap) > k:
                heapq.heappop(self.heap)
        while self.heap:
            dist, x, y = heapq.heappop(self.heap)
            ans.append([x, y])
        return ans

        
        
        

        