class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        rows = len(heights)
        cols = len(heights[0])
        ans = []
        for i in range(cols):
            pacific.add((0,i))
            atlantic.add((rows - 1, i))
        for j in range(rows):
            pacific.add((j, 0))
            atlantic.add((j, cols - 1))
        for _ in range(13):
            for i in range(rows):
                for j in range(cols):
                    explore = [[-1, 0], [1, 0], [0, -1], [0, 1]]
                    for each in explore:
                        dx, dy = each
                        x = i + dx
                        y = j + dy
                        if 0 <= x < rows and 0 <= y < cols and heights[i][j] >= heights[x][y]:
                            if (x,y) in pacific:
                                pacific.add((i, j))
                            if (x,y) in atlantic:
                                atlantic.add((i, j))
        for each in pacific:
            if each in atlantic:
                ans.append(list(each))
        return ans

        