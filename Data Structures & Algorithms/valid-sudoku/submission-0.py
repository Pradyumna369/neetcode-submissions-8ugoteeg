class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(dict)
        columns = defaultdict(dict)
        boxes = defaultdict(dict)

        for i in range(9):
            rows[i] = {}
            columns[i] = {}
            boxes[i] = {}
        
        def returnBox(row, column):
            box = (row // 3) * 3 + (column // 3)
            return box

        for row, arr in enumerate(board):
            for column, number in enumerate(arr):
                box = returnBox(row, column)
                if number != "." and (number in rows[row] or number in columns[column] or number in boxes[box]):
                    return False
                else:
                    rows[row][number] = True
                    columns[column][number] = True
                    boxes[box][number] = True
        return True
                
        