class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        soln = []
        posDiag = set()
        negDiag = set()
        occupiedCols = set()
        row = ""
        for i in range(n):
            row += "."
        # def possible(position): Giving n * n! time complexity. Extra n for checking diagonals
        #     r, c = position
        #     for each in occupied:
        #         oR, oC = each
        #         if abs(r - oR) == abs(c - oC):
        #             return False
        #     return True

        def dfs(i): # Recursively explores all possible columns to place a queen in the ith row
            if i >= n:
                res.append(soln[:])
                return
            for each in range(n):
                if each not in occupiedCols and (i + each) not in posDiag and (i - each) not in negDiag:
                    # if possible([i, each]):
                        row = ""
                        for col in range(n):
                            if col == each:
                                row += "Q"
                            else:
                                row += "."
                        soln.append(row)
                        # occupied.add((i, each))
                        posDiag.add(i + each)
                        negDiag.add(i - each)
                        occupiedCols.add(each)
                        dfs(i + 1)
                        soln.pop()
                        occupiedCols.remove(each)
                        posDiag.remove(i + each)
                        negDiag.remove(i - each)
                        # occupied.remove((i, each))
        dfs(0)
        return res
