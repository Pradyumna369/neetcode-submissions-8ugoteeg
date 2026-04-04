class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def maxAmount(i):
            if i == 0:
                return nums[0]
            if i == 1:
                return max(nums[0], nums[1])
            if i in memo:
                return memo[i]
            amount = max(nums[i] + maxAmount(i - 2), maxAmount(i - 1))
            memo[i] = amount
            return amount
        return maxAmount(len(nums) - 1)