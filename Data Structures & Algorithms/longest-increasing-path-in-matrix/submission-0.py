class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [[-1] * (n) for _ in range(m)]

        longest = 1

        def dfs(i, j):
            if dp[i][j] != -1:
                return dp[i][j]

            queue = deque()
            
            queue.append([i, j])
            
            maxLength = 0

            levels = 0
            while queue:
                levels += 1
                for _ in range(len(queue)):
                    length = 0
                    row, col = queue.popleft()
                    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
                    for each in directions:
                        dx, dy = each
                        x = row + dx
                        y = col + dy

                        if 0 <= x and x < m and 0 <= y and y < n:
                            if matrix[x][y] > matrix[row][col]:
                                if dp[x][y] != -1:
                                    length = max(length, dp[x][y])
                                else:
                                    queue.append([x, y])
                    maxLength = max(maxLength, levels + length)
            
            return maxLength
                        


        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                longest = max(longest, dfs(i, j))
        
        return longest
        
