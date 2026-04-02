class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = [[], 0]
        def comb(idx):
            if subset[1] == target:
                res.append(subset[0][:])
                return
            if idx >= len(nums):
                return
            if subset[1] > target:
                return
            subset[0].append(nums[idx])
            subset[1] += nums[idx]
            comb(idx)
            subset[0].pop()
            subset[1] -= nums[idx]
            comb(idx + 1)
        comb(0)
        return res