class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        '''
        ans = []
        m = 2
        open = 0
        curr = ''
        backtrack(0, 0, '()()'))        
        '''
        open = 0
        m = n
        ans = []
        def backtrack(m, open, curr):
            if m == 0 and open == 0:
                ans.append(curr)
            if m > 0:
                backtrack(m - 1, open + 1, curr + '(')
            if open > 0:
                backtrack(m, open - 1, curr + ')')
        backtrack(m, open, '')
        return ans

