class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sCounter = Counter(s)
        tCounter = Counter(t)

        for char in sCounter:
            if char not in tCounter or sCounter[char] != tCounter[char]:
                return False
        return True if len(sCounter) == len(tCounter) else False
                
        