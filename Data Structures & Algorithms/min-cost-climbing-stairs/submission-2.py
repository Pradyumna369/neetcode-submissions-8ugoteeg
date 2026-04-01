class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        curr = len(cost)
        price = 0
        while curr > 1:
            if cost[curr - 2] <= cost[curr - 1]:
                curr = curr - 2
            else:
                curr = curr - 1
            price += cost[curr]
        return price


