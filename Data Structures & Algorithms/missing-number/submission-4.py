class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # total = 0
        # for n in nums:
        #     total += n
        # l = len(nums)
        # actualSum = l * (l + 1) // 2
        # return actualSum - total

        # res = len(nums)
        # for i in range(len(nums)):
        #     res += i - nums[i]
        # return res

        n = len(nums)
        xorr = n
        for i in range(n):
            #XOR of same number cancels itself resulting in 0. XOR of a number with 0 gives the same number.
            xorr ^= i ^ nums[i]
        return xorr



        