class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.seen = set()
        first = word[0]
        l = len(board)
        def wordExists(index, element, seen):
            if index == len(word) - 1:
                return True
            row, col = element
            explore = [[-1,0], [1,0], [0,-1], [0,1]]
            for each in explore:
                dx, dy = each
                x = col + dx
                y = row + dy
                if (y, x) not in seen and 0 <= x < len(board[0]) and 0 <= y < len(board):
                    if board[y][x] == word[index + 1]:
                        seen.add((y, x))
                        if wordExists(index + 1, [y, x], seen):
                            return True
                        seen.remove((y,x))
            
                    

        for ind, row in enumerate(board):
            for col, char in enumerate(row):
                if char == first:
                    self.seen.add((ind, col))
                    if wordExists(0, [ind, col], self.seen):
                        return True
                    else:
                        self.seen.clear()
        return False

