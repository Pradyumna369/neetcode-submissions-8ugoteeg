class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        l, r = 0, len(matrix[0]) - 1
        top, bottom = 0, len(matrix) - 1
        
        while l <= r and top <= bottom:
            for i in range(r - l + 1):
                res.append(matrix[top][l + i])
            top += 1
            for j in range(bottom - top + 1):
                res.append(matrix[top + j][r])
            r -= 1
            if not (l <= r and top <= bottom):
                break
            for k in range(r - l + 1):
                res.append(matrix[bottom][r - k])
            bottom -= 1
            for m in range(bottom, top - 1, -1):
                res.append(matrix[m][l])
            l += 1
        return res
