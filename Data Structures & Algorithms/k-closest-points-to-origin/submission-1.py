class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(point):
            x, y = point
            distance = x ** 2 + y ** 2
            return distance
        self.heap = []
        ans = []
        for point in points:
            dist = distance(point)
            heapq.heappush(self.heap, [-dist, point])
            if len(self.heap) > k:
                heapq.heappop(self.heap)
        while self.heap:
            dist, point = heapq.heappop(self.heap)
            ans.append(point)
        return ans

        
        
        

        