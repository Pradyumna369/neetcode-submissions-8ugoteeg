class Solution:
    def findMin(self, nums: List[int]) -> int:
        # rotated array has one special property. One part is always sorted and other contains rotation with min element.
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            # Part of array which is always sorted. return left most element
            if nums[mid] <= nums[r] and nums[l] <= nums[mid]:
                return nums[l]
            # Part which contains rotation. Smallest in between left and right elements
            elif nums[mid] >= nums[l]:
                l = mid + 1
            elif nums[mid] <= nums[r]:
                r = mid
        return nums[l]