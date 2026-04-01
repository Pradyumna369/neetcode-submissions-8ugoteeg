from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        tOriginal = Counter(t)
        tAct = Counter(t)
        chars = set(t)
        left = 0
        sub = ""
        min_len = float('inf')

        for right in range(len(s)):
            if s[right] in tAct:
                tAct[s[right]] -= 1
                # When we’ve satisfied a char requirement, remove it from set
                if tAct[s[right]] == 0:
                    chars.remove(s[right])
            
            # When all required chars are covered
            while len(chars) == 0:
                # Update smallest substring
                if (right - left + 1) < min_len:
                    min_len = right - left + 1
                    sub = s[left:right + 1]

                # Try to shrink from left
                if s[left] in tAct:
                    tAct[s[left]] += 1
                    # If we’ve gone below the required count, add back to chars
                    if tAct[s[left]] > 0:
                        chars.add(s[left])
                left += 1
        
        return sub
