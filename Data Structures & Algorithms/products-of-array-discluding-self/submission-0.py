class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        2 <= nums.length <= 1000
        -20 <= nums[i] <= 20
        nums = [1, 2, 4, 6]
                   ^
        mulleft = [1, 2, 8, 48]
        mulright = [48, 48, 24, 6]
        ans = [48, 24, 12, 8]
        '''
        mulleft = [1] * len(nums)
        mulright = [1] * len(nums)
        prev = 1
        for i, num in enumerate(nums):
            mulleft[i] = prev
            prev *= num
        prev = 1
        for i in range(len(nums) - 1, -1 ,-1):
            mulright[i] = prev
            prev *= nums[i]
        ans = [1] * len(nums)
        for i in range(len(nums)):
            ans[i] = mulleft[i] * mulright[i]
        return ans