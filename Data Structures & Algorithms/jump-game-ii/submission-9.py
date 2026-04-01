class Solution:
    def jump(self, nums: List[int]) -> int:
        # cur = 0
        # later = 0
        # count = 0
        # if len(nums) == 1:
        #     return 0
        # while cur < len(nums):
        #     longest = 0
        #     for j in range(1, nums[cur] + 1):
        #         if cur + j >= len(nums) - 1:
        #             return count + 1
        #         if cur + j + nums[cur + j] > longest:
        #             later = cur + j
        #             longest = cur + j + nums[cur + j]
        #     cur = later
        #     count += 1
        # return count

        # near = far = jumps = 0

        # while far < len(nums) - 1:
        #     farthest = 0
        #     for i in range(near, far + 1):
        #         farthest = max(farthest, i + nums[i])
        #     near = far
        #     jumps += 1
        #     far = farthest
        # return jumps

        jumps = cur_end = cur_farthest = 0

        for i in range(len(nums) - 1):
            cur_farthest = max(cur_farthest, i + nums[i])

            if i == cur_end:
                jumps += 1
                cur_end = cur_farthest
        return jumps





