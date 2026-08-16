class MyStack:

    def __init__(self):
        self.first = []
        self.second = []
        self.count = 0

    def push(self, x: int) -> None:
        self.first.append(x)
        self.count += 1

    def pop(self) -> int:
        for _ in range(self.count - 1):
            value = self.first.pop(0)
            self.second.append(value)
        
        self.count -= 1

        self.first, self.second = self.second, self.first
        return self.second.pop(0)

        

    def top(self) -> int:
        value = 0
        for _ in range(self.count):
            value = self.first.pop(0)
            self.second.append(value)
        
        self.first, self.second = self.second, self.first
        return value
        

    def empty(self) -> bool:
        if self.count == 0:
            return True
        else:
            return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()