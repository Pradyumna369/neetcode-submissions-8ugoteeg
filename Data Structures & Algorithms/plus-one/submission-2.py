class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # l = len(digits)
        # num = 0
        # for ind, digit in enumerate(digits):
        #     num += digit * (10 ** (l - ind - 1))
        # total = num + 1
        # res = []
        # while total > 0:
        #     res.append(total % 10)
        #     total = total // 10
        # res.reverse()
        # return res

        digits = digits[::-1]
        carry, i = 1, 0

        while carry:
            if i < len(digits):
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    carry = 0
            else:
                digits.append(1)
                carry = 0
            i += 1
        digits = digits[::-1]
        return digits