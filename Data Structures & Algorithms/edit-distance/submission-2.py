class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        '''
Other way of looking at the soln
dfs(i, j) = min operations to convert word1[i:] to word2[j:].

Match → no operation needed, move both forward → dfs(i+1, j+1)
No match → try all 3 operations, add 1, take minimum:

Delete word1[i] → i moves, j stays (still unmatched) → dfs(i+1, j)
Insert word2[j] → inserting the exact character, so j is satisfied, moves forward, i stays → dfs(i, j+1)
Replace word1[i] with word2[j] → both matched, both move → dfs(i+1, j+1)


All 3 branches are always explored, min() picks the cheapest. 
Branches that never find a match don't fail — base cases act as the safety net, 
paying the full cost of remaining characters:

word1 exhausted → insert all remaining word2 → n - j
word2 exhaused → delete all remaining word1 → m - i
        '''
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
        