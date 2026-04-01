class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        pairs = list(c.items())
        pairs.sort(key = lambda x: -x[1])
        ans = []
        for i in range(k):
            ans.append(pairs[i][0])
        return ans

        