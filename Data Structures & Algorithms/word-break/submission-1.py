class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [True] + len(s) * [False]
        for i in range(1, len(s) + 1):
            for w in wordDict:
                start = i - len(w)
                if start >= 0 and s[start : i] == w and dp[start]:
                    dp[i] = True

        return dp[-1]
