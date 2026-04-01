class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        curr = 1
        maxProfit = 0
        while curr < len(prices):
            profit = prices[curr] - buy
            buy = min(buy, prices[curr])
            maxProfit = max(profit, maxProfit)
            curr += 1
        return maxProfit




            
        