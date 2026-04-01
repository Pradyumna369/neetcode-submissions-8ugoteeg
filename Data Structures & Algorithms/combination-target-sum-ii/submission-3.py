class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        count = defaultdict(list)
        for idx, candidate in enumerate(candidates):
            count[candidate].append(idx)

        def makeCombinations(idx, comb, total, contains):
            if total == target:
                res.append(comb[:])
                return
            if idx >= len(candidates) or total > target:
                return
            # contains = Counter(comb)
            num = candidates[idx]
            if contains[num] < count[num].index(idx):
                makeCombinations(idx + 1, comb, total, contains)
                return
            comb.append(candidates[idx])
            contains[num] += 1
            makeCombinations(idx + 1, comb, total + candidates[idx], contains)
            comb.pop()
            contains[num] -= 1
            makeCombinations(idx + 1, comb, total, contains)
        contains = defaultdict(int)
        makeCombinations(0,[],0, contains)
        return res
        