class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            # XOR operator ^ between two same bits gives 0 as a result or else 1 if different
            res = num ^ res
        return res