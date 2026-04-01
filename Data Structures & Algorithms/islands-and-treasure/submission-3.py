class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        def expand(treasure):
            queue = deque()
            queue.append(treasure)
            while queue:
                row, col = queue.popleft()
                explore = [[-1, 0], [1, 0], [0, -1], [0, 1]]
                for each in explore:
                    dx, dy = each
                    x = row + dx
                    y = col + dy
                    if 0 <= x < rows and 0 <= y < cols and grid[x][y] != 0:
                        if grid[x][y] > grid[row][col] + 1:
                            queue.append([x, y])
                            grid[x][y] = grid[row][col] + 1

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0: # Multi level BFS, one from each treasure
                    expand([r,c])
        