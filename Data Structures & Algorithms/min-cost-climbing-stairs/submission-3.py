class Solution:
    def __init__(self):
        self.min = {}

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        l = len(cost)

        def dp(i):
            if i <= 1:
                return 0
            
            if i in self.min:
                return self.min[i]
            
            self.min[i] = min(cost[i - 1] + dp(i - 1), cost[i - 2] + dp(i - 2))
            return self.min[i]
        
        return dp(l)