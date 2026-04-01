class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {} # key=(i, canBuy) val=max_profit

        def dfs(i, canBuy):
            if i >= len(prices):
                return 0
            
            if (i, canBuy) in dp:
                return dp[(i, canBuy)]
            
            cooldown = dfs(i + 1, canBuy)
            if canBuy:
                buy = dfs(i + 1, not canBuy) - prices[i]
                dp[(i, canBuy)] = max(buy, cooldown)
            else:
                sell = dfs(i + 2, not canBuy) + prices[i]
                dp[(i, canBuy)] = max(sell, cooldown)
            
            return dp[(i, canBuy)]
        
        return dfs(0, True)