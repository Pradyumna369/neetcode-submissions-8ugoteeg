class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # maxSub, curSum = nums[0], 0
        # for num in nums:
        #     if curSum < 0:  # If the sub-array has more negatives than positives, discard that
        #         curSum = 0
        #     curSum += num
        #     maxSub = max(maxSub, curSum)
        # return maxSub

        maxSub, curSum = nums[0], 0
        for num in nums:
            if curSum <0:
                curSum = 0
            curSum += num
            maxSub = max(maxSub, curSum)
        return maxSub