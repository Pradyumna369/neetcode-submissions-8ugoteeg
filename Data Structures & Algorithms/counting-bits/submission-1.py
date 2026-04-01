class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        offset = 1
        # offset is the number with the same most siginficant bit (number with 1 in the same left most position as this number)
        # offset of 2 and 3 is 2 (2: 010, 3: 011. most significant bit is in 2nd position same for both). 
        # The pattern just repeats for every offset. so using a dp
        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]
        return dp
