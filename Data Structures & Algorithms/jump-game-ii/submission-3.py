class Solution:
    def jump(self, nums: List[int]) -> int:
        cur = 0
        later = 0
        count = 0
        if len(nums) == 1:
            return 0
        while cur < len(nums):
            longest = 0
            for j in range(1, nums[cur] + 1):
                if cur + j >= len(nums) - 1:
                    return count + 1
                if cur + j + nums[cur + j] > longest:
                    later = cur + j
                    longest = cur + j + nums[cur + j]
            cur = later
            count += 1
        return count