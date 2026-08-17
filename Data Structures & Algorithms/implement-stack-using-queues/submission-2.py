class MyStack:

    def __init__(self):
        self.first = []
        self.second = []

    def push(self, x: int) -> None:
        self.first.append(x)

    def pop(self) -> int:
        for _ in range(len(self.first) - 1):
            value = self.first.pop(0)
            self.second.append(value)
        
        self.first, self.second = self.second, self.first
        return self.second.pop(0)

        

    def top(self) -> int:
        value = 0
        for _ in range(len(self.first)):
            value = self.first.pop(0)
            self.second.append(value)
        
        self.first, self.second = self.second, self.first
        return value
        

    def empty(self) -> bool:
        if len(self.first) == 0:
            return True
        else:
            return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()