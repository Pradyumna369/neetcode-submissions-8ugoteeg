class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        """
        s = "rabbbit"
        t = "rabbit"

            r a b b b i t
          1 1 1 1 1 1 1 1
        r 0 1 1 1 1 1 1 1
        a 0 0 1 1 1 1 1 1
        b 0 0 0 1 2 3 3 3
        b 0 0 0 0 1 3 3 3
        i 0 0 0 0 0 0 3 3
        t 0 0 0 0 0 0 0 3

        m = 5
        n = 6
        """
        m = len(t)
        n = len(s)
        matrix = [[0] * (n + 1) for _ in range(m + 1)]
        for k in range(n + 1):
            matrix[0][k] = 1
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if t[i - 1] == s[j - 1]:
                    matrix[i][j] = matrix[i][j - 1] + matrix[i - 1][j - 1]
                else:
                    matrix[i][j] = matrix[i][j - 1]
        return matrix[m][n]

