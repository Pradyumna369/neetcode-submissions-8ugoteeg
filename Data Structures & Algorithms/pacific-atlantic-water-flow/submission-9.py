class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        rows = len(heights)
        cols = len(heights[0])
        ans = []

        def dfs(row, col, visit, prevHeight):
            if (row < 0 or row >= rows or col < 0 or col >= cols or 
            heights[row][col] < prevHeight or (row, col) in visit):
                return
            visit.add((row, col))
            explore = [[-1, 0], [1, 0], [0, -1], [0, 1]]
            for each in explore:
                dx, dy = each
                x, y = row + dx, col + dy
                dfs(x, y, visit, heights[row][col])

        for i in range(cols):
            dfs(0, i, pacific, heights[0][i])
            dfs(rows - 1, i, atlantic, heights[rows - 1][i])
        for j in range(rows):
            dfs(j, 0, pacific, heights[j][0])
            dfs(j, cols - 1, atlantic, heights[j][cols - 1])
        
        
        for each in pacific:
            if each in atlantic:
                ans.append(list(each))
        return ans
