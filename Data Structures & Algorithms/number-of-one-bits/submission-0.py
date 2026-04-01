class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        # Method 1
        # while n:
        #     res += 1 if n & 1 else 0
        #     n >>= 1
        # return res
        while n:
            n &= n - 1
            res += 1
        return res
