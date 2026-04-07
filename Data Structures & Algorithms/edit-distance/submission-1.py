class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        dp = {}
        def dfs(i, j):  # represents the min number of operations needed to convert word1[i:] into word2[j:]
            if i == m:  # if i reached end of word1, add remaining characters
                return n - j
            if j == n:  # if j reaches end of word2, remove remaining characters
                return m - i

            if (i, j) in dp:    # returning the cached result
                return dp[(i, j)]
            
            if word1[i] == word2[j]:    # if both characters are same, no need of any operation
                dp[(i, j)] = dfs(i + 1, j + 1)
            else:                       # otherwise consider three operations
                res = min(dfs(i + 1, j), dfs(i, j + 1)) # delete from word1, insert into word1
                res = min(res, dfs(i + 1, j + 1))       # replace the character
                dp[(i, j)] = res + 1                    # take min of 3 and add 1 for current operation
            return dp[(i, j)]
        
        return dfs(0, 0)