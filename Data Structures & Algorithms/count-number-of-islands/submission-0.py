class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        rows, cols = len(grid), len(grid[0])
        visited = set()
        def isIsland(cell, seen):
            row, col = cell
            if (row, col) in seen or row < 0 or row >= rows or col < 0 or col >= cols or (row, col) in visited:
                return
            visited.add((row, col))
            seen.add((row, col))
            if grid[row][col] == "1":
                isIsland((row + 1, col), seen)
                isIsland((row - 1, col), seen)
                isIsland((row, col + 1), seen)
                isIsland((row, col - 1), seen)      

        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visited and grid[r][c] == "1":
                    isIsland((r, c), set())
                    islands += 1
                visited.add((r,c))
        return islands
