class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[l] <= nums[mid] <= nums[r]:
                break
            elif nums[l] <= nums[mid]:
                l = mid + 1
            elif nums[mid] <= nums[r]:
                r = mid
        lowest = l
        if lowest == 0:
            l, r = 0, len(nums) - 1
        elif target >= nums[0] and target <= nums[lowest - 1]:
            r, l = lowest - 1, 0
        elif target >= nums[lowest]:
            l, r = lowest, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if target <= nums[mid]:
                r = mid
            else:
                l = mid + 1
        return l if nums[l] == target else -1
