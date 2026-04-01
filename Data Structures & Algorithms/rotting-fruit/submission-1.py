class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time = 0
        rows, cols = len(grid), len(grid[0])
        rotten = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    rotten.append((r,c))
        while rotten:
            time += 1
            for _ in range(len(rotten)):
                row, col = rotten.popleft()
                explore = [[-1, 0], [1, 0], [0, -1], [0, 1]]
                for each in explore:
                    dx, dy = each
                    x, y = row + dx, col + dy
                    if 0 <= x < rows and 0 <= y < cols and grid[x][y] == 1:
                        grid[x][y] = 2
                        rotten.append((x, y))
            
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1
        return time - 1 if time > 0 else 0
        