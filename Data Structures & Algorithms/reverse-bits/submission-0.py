class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        pos = 1
        while n:
            res += (2 ** (32 - pos)) * (1 if n & 1 else 0)
            n >>= 1
            pos += 1
        return res
        