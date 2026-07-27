class MinStack:

    def __init__(self):
        self.stack = []
        self.min = float("inf")
        

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.min = val
        else:
            self.stack.append(val - self.min)
            self.min = min(val, self.min)
        

    def pop(self) -> None:
        value = self.stack.pop()

        if value < 0:
            self.min = self.min - value
        

    def top(self) -> int:
        value = self.stack[-1]

        if value > 0:
            return self.min + value
        else:
            return self.min

    def getMin(self) -> int:
        return self.min
        
