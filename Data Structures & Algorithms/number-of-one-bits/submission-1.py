class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        # Method 1
        # while n:
        #    #  & with 1 turns last bit to 1 if it is 1 or else 0 if it is 0    
        #     res += 1 if n & 1 else 0
        #     n >>= 1
        # return res
        while n:
            # n & n - 1 converts right-most bit to 0 and every 0s right of it to 1s and their & turns all of them to 0s.
            # So each bit is picked exactly once
            n &= n - 1
            res += 1
        return res
