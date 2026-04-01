class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        count = defaultdict(list)
        for idx, candidate in enumerate(candidates):
            count[candidate].append(idx)

        def makeCombinations(idx, comb, total):
            if total == target:
                res.append(comb[:])
                return
            if idx >= len(candidates) or total > target:
                return
            contains = Counter(comb)
            num = candidates[idx]
            if contains[num] < count[num].index(idx):
                makeCombinations(idx + 1, comb, total)
                return
            comb.append(candidates[idx])
            makeCombinations(idx + 1, comb, total + candidates[idx])
            comb.pop()
            makeCombinations(idx + 1, comb, total)
        makeCombinations(0,[],0)
        return res
        