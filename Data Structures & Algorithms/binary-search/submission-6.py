class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n - 1
        while l < r:
            mid = (l + r) // 2
            if target <= nums[mid]:
                r = mid
            else:
                l = mid + 1
        return l if nums[l] == target else -1
        