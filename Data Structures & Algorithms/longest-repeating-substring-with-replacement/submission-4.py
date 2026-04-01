class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        chars = defaultdict(int)
        l = len(s)
        maxSub = 1
        # maxf = 0
        while right < l:
            chars[s[right]] += 1
            # maxf = max(maxf, chars[s[right]])
            # Need not calculate everytime maxf decreases, 
            # because decreasing it would mean smaller string which we need not consider
            # as we already calculated a larger substring length
            while ((right - left + 1) - max(chars.values()))  > k:
            # while (right - left + 1) - maxf > k:   
                chars[s[left]] -= 1
                left += 1
            maxSub = max(maxSub, right - left + 1)
            right += 1
        return maxSub