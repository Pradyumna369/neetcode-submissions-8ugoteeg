class Solution:
    def __init__(self):
        self.memo = {}
    def climbStairs(self, n: int) -> int:
        if n == 1:  # Base cases
            return 1
        if n == 2:
            return 2

        if n in self.memo:  # Returning from optimal substructure
            return self.memo[n]
        
        self.memo[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)    # Memoization

        return self.climbStairs(n)