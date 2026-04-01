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

        def dfs(i, comb, total):
            if total == target:
                res.append(comb[:])
                return
            if total > target or i == len(candidates):
                return
            comb.append(candidates[i])
            dfs(i + 1, comb, total + candidates[i]) # Exploring with current number
            comb.pop()  # Backtracking to explore without current number

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, comb, total)
        dfs(0,[],0)
        return res


