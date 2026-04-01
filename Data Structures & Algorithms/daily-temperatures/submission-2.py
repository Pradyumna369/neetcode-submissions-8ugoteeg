class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # ans = []
        # for ind, temp in enumerate(temperatures):
        #     day = 0
        #     for higher in range(ind + 1, len(temperatures)):
        #         if temperatures[higher] > temp:
        #             day = higher - ind
        #             break
        #     ans.append(day)
        # return ans
        ans = []
        l = len(temperatures)
        stack = [[temperatures[-1], l - 1]]
        for i in range(l - 1, -1, -1):
            while stack and temperatures[i] >= stack[-1][0]:
                stack.pop()
            if stack:
                ans.append(stack[-1][1] - i)
            else:
                ans.append(0)
            stack.append([temperatures[i], i])
        return ans[::-1]

