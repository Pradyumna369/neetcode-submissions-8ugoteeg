class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        l = len(grid)
        first = grid[0][0]
        last = grid[l - 1][l - 1]
        minTime = max(first, last)
        maxTime = minTime
        for i in range(l):
            for j in range(l):
                maxTime = max(maxTime, grid[i][j])
        def canSwim(t):
            visited = set((0, 0))
            def dfs(point):
                px, py = point
                if px == py == l - 1:
                    return True
                explore = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for each in explore:
                    dx, dy = each
                    x, y = px + dx, py + dy
                    if 0 <= x < l and 0 <= y < l and (x, y) not in visited and grid[x][y] <= t:
                        visited.add((x, y))
                        if dfs((x, y)): return True
            return dfs((0, 0))
        while minTime < maxTime:
            mid = (minTime + maxTime) // 2
            if canSwim(mid):
                maxTime = mid
            else:
                minTime = mid + 1
        return minTime


            

                    

            
