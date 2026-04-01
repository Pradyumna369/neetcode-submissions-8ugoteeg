class Solution:
    def isHappy(self, n: int) -> bool:
        numbers = set()
        def compute(n):
            total = 0
            while n != 0:
                total += (n % 10) ** 2
                n = n // 10
            if total in numbers:
                return False
            elif total == 1:
                return True
            else:
                numbers.add(total)
                return compute(total)
        return compute(n)


