import bisect
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        win = []
        ans = []
        for i in range(k):
            win.append(nums[i])
        win.sort()
        ans.append(win[-1])
        for curr in range(k, len(nums)):
            remInd = bisect.bisect_left(win, nums[curr - k])
            win.pop(remInd)
            insInd = bisect.bisect_right(win, nums[curr])
            win.insert(insInd, nums[curr])
            ans.append(win[-1])
        return ans  