class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        # count = defaultdict(list)
        # for idx, candidate in enumerate(candidates):
        #     count[candidate].append(idx)

        # def makeCombinations(idx, comb, total, contains):
        #     if total == target:
        #         res.append(comb[:])
        #         return
        #     if idx >= len(candidates) or total > target:
        #         return
        #     # contains = Counter(comb)
        #     num = candidates[idx]
        #     if contains[num] < count[num].index(idx):
        #         makeCombinations(idx + 1, comb, total, contains)
        #         return
        #     comb.append(candidates[idx])
        #     contains[num] += 1
        #     makeCombinations(idx + 1, comb, total + candidates[idx], contains)
        #     comb.pop()
        #     contains[num] -= 1
        #     makeCombinations(idx + 1, comb, total, contains)
        # contains = defaultdict(int)
        # makeCombinations(0,[],0, contains)
        # return res
        
        candidates.sort()

        def dfs(idx, comb, total):
            if total == target:
                res.append(comb[:])
            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                if total > target:
                    return
                comb.append(candidates[i])
                dfs(i + 1, comb, total + candidates[i])
                comb.pop()
        dfs(0,[],0)
        return res


