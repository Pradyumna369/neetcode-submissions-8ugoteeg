class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        self.heap = []
        for stone in stones:
            heapq.heappush(self.heap, -stone)
        while len(self.heap) > 1:
            heaviest = -(heapq.heappop(self.heap))
            heavier = - (heapq.heappop(self.heap))
            remaining = heaviest - heavier
            heapq.heappush(self.heap, -remaining)
        return -self.heap[0]
        