class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        '''
        num1 = "3"
        num = ord(c) - ord("0") + ord(0)
        '''
        
        num3 = 0
        for i in range(len(num1) - 1, -1, -1):
            num3 += pow(10, len(num1) - i - 1) * int(num1[i]) 
        num4 = 0
        for i in range(len(num2) - 1, -1, -1):
            num4 += pow(10, len(num2) - i - 1) * int(num2[i])

        return str(num3 * num4)
         