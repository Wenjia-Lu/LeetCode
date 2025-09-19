class MinStack:
    def __init__(self):
        self.stack = []
        self.history = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.stack) == 1:
            self.history.append(val)
        else:
            self.history.append(min(val, self.history[-1]))
        


    def pop(self) -> None:
        self.stack.pop()
        self.history.pop()



    def top(self) -> int:
        return self.stack[-1]
        
        
    def getMin(self) -> int:
        return self.history[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()