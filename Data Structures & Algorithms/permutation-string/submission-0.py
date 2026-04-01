class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = len(s1)
        countS1 = Counter(s1)
        left = right = 0
        countS2 = defaultdict(int)
        while right < len(s2):
            countS2[s2[right]] += 1
            if right - left + 1 > l:
                countS2[s2[left]] -= 1
                if countS2[s2[left]] == 0:
                    countS2.pop(s2[left])
                left += 1
            if countS2 == countS1:
                return True
            right += 1
        return False