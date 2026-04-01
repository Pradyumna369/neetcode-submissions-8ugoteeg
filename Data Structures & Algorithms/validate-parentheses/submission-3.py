class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {"(":")", "{":"}", "[":"]"}
        for bracket in s:
            if bracket in brackets:
                stack.append(brackets[bracket])
            else:
                if not stack or stack.pop() != bracket:
                    return False
        if stack:
            return False
        return True