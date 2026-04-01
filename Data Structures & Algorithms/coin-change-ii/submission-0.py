class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {} # key=(amount, coin_index) val=no_of_ways
        def dfs(amount, i):
            if amount == 0:
                return 1
            if amount < 0 or i == len(coins):
                return 0
            if (amount, i) in dp:
                return dp[(amount, i)]
            
            # Ways including current coin + ways excluding current coin
            ways = dfs(amount - coins[i], i) + dfs(amount, i + 1)
            
            dp[(amount, i)] = ways
            return ways
        return dfs(amount, 0)