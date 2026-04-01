class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        arr = [-1] * (amount + 1)
        if amount == 0:
            return 0
        for i, each in enumerate(arr):
            if i in coins:
                arr[i] = 1
                continue
            count = amount + 1
            for coin in coins:
                diff = i - coin
                if diff > 0 and arr[diff] != -1:
                    count = min(count, arr[diff] + 1)
            if count != amount + 1:
                arr[i] = count
        return arr[amount]
        

        

        