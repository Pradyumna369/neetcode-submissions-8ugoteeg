class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time = 0
        rows, cols = len(grid), len(grid[0])
        rotten = deque()
        fresh = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    rotten.append((r,c))
                if grid[r][c] == 1:
                    fresh += 1
        while rotten and fresh > 0:
            time += 1
            for _ in range(len(rotten)):
                row, col = rotten.popleft()
                explore = [[-1, 0], [1, 0], [0, -1], [0, 1]]
                for each in explore:
                    dx, dy = each
                    x, y = row + dx, col + dy
                    if 0 <= x < rows and 0 <= y < cols and grid[x][y] == 1:
                        grid[x][y] = 2
                        fresh -= 1
                        rotten.append((x, y))
            
        return time if fresh == 0 else -1
        