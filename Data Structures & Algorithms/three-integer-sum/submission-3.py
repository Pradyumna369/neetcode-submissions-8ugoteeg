class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        l = len(nums)
        for ind in range(l - 2):
            left = ind + 1
            right = l - 1
            target = -1 * nums[ind]
            while left < right:
                if nums[left] + nums[right] > target:
                    right -= 1
                elif nums[left] + nums[right] < target:
                    left += 1
                else:
                    triplet = [nums[ind], nums[left], nums[right]]
                    if triplet not in ans:
                        ans.append(triplet)
                    left += 1
                    
                    
        return ans
      