class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        res = [0] * (len(nums))
        available = nums[:]
        def permutate(i):
            if i > len(nums) - 1:
                ans.append(res[:])
                return
            for idx, each in enumerate(available):
                res[i] = each
                available.remove(each)
                permutate(i + 1)
                available.insert(idx, each)
                res[i] = 0
        permutate(0)
        return ans

