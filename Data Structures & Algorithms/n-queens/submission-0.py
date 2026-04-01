class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        soln = []
        occupied = set()
        row = ""
        for i in range(n):
            row += "."
        def possible(position):
            r, c = position
            for each in occupied:
                oR, oC = each
                if c == oC:
                    return False
                if abs(r - oR) == abs(c - oC):
                    return False
            return True

        def dfs(i):
            if i >= n:
                res.append(soln[:])
                return
            for each in range(n):
                if possible([i, each]):
                    row = ""
                    for col in range(n):
                        if col == each:
                            row += "Q"
                        else:
                            row += "."
                    soln.append(row)
                    occupied.add((i, each))
                    dfs(i + 1)
                    soln.pop()
                    occupied.remove((i, each))
        dfs(0)
        return res
