class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            # XOR operator ^ between two same bits gives 0 as a result or else 1 if different (0 and 1)
            # a ^ 0 = a, a ^ a = 0
            res = num ^ res
        return res