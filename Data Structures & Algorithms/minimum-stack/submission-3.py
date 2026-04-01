class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        minimum = self.getMin()
        if minimum is None or val < minimum:
            minimum = val
        self.stack.append([val, minimum])

    def pop(self) -> None:
        return self.stack.pop()[0]

    def top(self) -> int:
        return self.stack[-1][0] if self.stack else None

    def getMin(self) -> int:
        return self.stack[-1][1] if self.stack else None
        
