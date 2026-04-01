class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.maxArea = 0
        rows, cols = len(grid), len(grid[0])
        def findArea(position):
            row, col = position
            queue = deque()
            queue.append((row, col))
            area = 0
            grid[row][col] = 0
            while queue:
                cur = queue.popleft()
                area += 1
                self.maxArea = max(self.maxArea, area)
                x, y = cur
                explore = [[-1, 0], [0, -1], [1, 0], [0, 1]]
                for each in explore:
                    dx, dy = each
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                        queue.append((nx, ny))
                        grid[nx][ny] = 0
        for row, each in enumerate(grid):
            for col, val in enumerate(each):
                if val == 1:
                    findArea([row, col])
                    grid[row][col] = 0
        return self.maxArea
    
            


        