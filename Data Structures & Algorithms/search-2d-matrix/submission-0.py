class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        t, b = 0, m - 1
        while t < b:
            mid = (t + b + 1) // 2
            if target < matrix[mid][0]:
                b = mid - 1
            else:
                t = mid
        l, r = 0, n - 1
        while l < r:
            mid = (l + r) // 2
            if target <= matrix[t][mid]:
                r = mid
            else:
                l = mid + 1
        return matrix[t][l] == target 