class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        maxProfit = 0
        for sell in prices:
            profit = sell - buy
            buy = min(buy, sell)
            maxProfit = max(profit, maxProfit)
        return maxProfit




            
        