class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers = {}
        # for ind, num in enumerate(nums):
        #     numbers[num] = ind
        # for ind,num in enumerate(nums):
        #     if target - num in numbers and numbers[target - num] != ind:
        #         return [ind, numbers[target - num]]

        for ind, num in enumerate(nums):
            difference = target - num
            if difference in numbers:
                return [numbers[difference], ind]
            numbers[num] = ind
        