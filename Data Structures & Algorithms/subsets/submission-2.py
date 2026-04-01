class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        # def makeCombinations(idx, comb):
        #     if idx >= len(nums):
        #         return
        #     comb.append(nums[idx])  # Using same index
        #     res.append(comb[:])
        #     makeCombinations(idx + 1, comb) # Explore that combination
        #     comb.pop()              # Backtrack
        #     makeCombinations(idx + 1, comb) # Second combination
        # res.append([])
        # makeCombinations(0, [])
        # return res
        subset = []

        def makeCombinations(idx):
            if idx >= len(nums):
                res.append(subset[:])
                return
            subset.append(nums[idx])
            makeCombinations(idx + 1)
            subset.pop()
            makeCombinations(idx + 1)
        makeCombinations(0)
        return res
        