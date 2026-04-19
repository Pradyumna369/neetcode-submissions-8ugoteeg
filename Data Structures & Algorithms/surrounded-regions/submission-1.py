class Solution:
    def solve(self, board: List[List[str]]) -> None:
        '''
        1 <= board.length, board[i].length <= 200

        O -> i + 1, j + 1, i - 1, j - 1 -> within bounds
        else:
            whole region is not surrounded 
        '''
        m = len(board)
        n = len(board[0])

        seen = set()
        region = set()
        def modifyRegion(cell) -> None:
            row, col = cell
            seen.add((row, col))
            region.add((row, col))
            cells = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for each in cells:
                dx, dy = each
                x, y = row + dx, col + dy
                if 0 <= x < m and 0 <= y < n and board[x][y] == 'O' and (x, y) not in region:
                    if not modifyRegion((x, y)):
                        return False
                elif x == -1 or x == m or y == -1 or y == n:
                    return False
            return True

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and board[i][j] not in seen:
                    if modifyRegion((i, j)):
                        for each in region:
                            x, y = each
                            board[x][y] = 'X'
                region.clear()
        
