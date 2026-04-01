class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = []
        for ind, temp in enumerate(temperatures):
            day = 0
            for higher in range(ind + 1, len(temperatures)):
                if temperatures[higher] > temp:
                    day = higher - ind
                    break
            ans.append(day)
        return ans