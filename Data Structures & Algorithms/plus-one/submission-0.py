class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        l = len(digits)
        num = 0
        for ind, digit in enumerate(digits):
            num += digit * (10 ** (l - ind - 1))
        total = num + 1
        res = []
        while total > 0:
            res.append(total % 10)
            total = total // 10
        res.reverse()
        return res