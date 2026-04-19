class Solution:
    def solve(self, board: List[List[str]]) -> None:
        '''
        1 <= board.length, board[i].length <= 200

        O -> i + 1, j + 1, i - 1, j - 1 -> within bounds
        else:
            whole region is not surrounded 
        '''
        ROWS, COLS = len(board), len(board[0])

        def capture(r, c):
            if (r < 0 or c < 0 or r == ROWS or
                c == COLS or board[r][c] != "O"
            ):
                return
            board[r][c] = "T"
            capture(r + 1, c)
            capture(r - 1, c)
            capture(r, c + 1)
            capture(r, c - 1)

        for r in range(ROWS):
            if board[r][0] == "O":
                capture(r, 0)
            if board[r][COLS - 1] == "O":
                capture(r, COLS - 1)

        for c in range(COLS):
            if board[0][c] == "O":
                capture(0, c)
            if board[ROWS - 1][c] == "O":
                capture(ROWS - 1, c)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"

        # m = len(board)
        # n = len(board[0])

        # seen = set()
        # region = set()
        # def modifyRegion(cell) -> None:
        #     row, col = cell
        #     seen.add((row, col))
        #     region.add((row, col))
        #     cells = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        #     for each in cells:
        #         dx, dy = each
        #         x, y = row + dx, col + dy
        #         if 0 <= x < m and 0 <= y < n and board[x][y] == 'O' and (x, y) not in region:
        #             if not modifyRegion((x, y)):
        #                 return False
        #         elif x == -1 or x == m or y == -1 or y == n:
        #             return False
        #     return True

        # for i in range(m):
        #     for j in range(n):
        #         if board[i][j] == 'O' and board[i][j] not in seen:
        #             if modifyRegion((i, j)):
        #                 for each in region:
        #                     x, y = each
        #                     board[x][y] = 'X'
        #         region.clear()
        
