class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        chars = defaultdict(int)
        l = len(s)
        maxSub = 1
        while right < l:
            chars[s[right]] += 1
            highest = max(chars.values())
            dist = right - left + 1 - highest 
            while dist > k and left <= right:
                chars[s[left]] -= 1
                left += 1
                highest = max(chars.values())
                dist = right - left + 1 - highest
            maxSub = max(maxSub, right - left + 1)
            right += 1
        return maxSub