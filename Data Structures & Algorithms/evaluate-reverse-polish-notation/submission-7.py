class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        '''
        1 <= tokens.length <= 1000
        -100 <= integer <= 100
        tokens = ['10','6','9','3','+','-11','*','/','*''17','+','5','+']
                    ^                   
        stack = [10, 6, -132, ]
        ans = 9 - 4 = 5
        '''
        stack = []
        operations = ['+', '-', '*', '/']
        for token in tokens:
            if token in operations:
                operand = token
                second = stack.pop()
                first = stack.pop()
                if operand == '+':
                    result = first + second
                elif operand == '-':
                    result = first - second
                elif operand == '*':
                    result = first * second
                else:
                    result = int(first / second)
                stack.append(result)
            else:
                stack.append(int(token))
        return stack.pop()

