class MinStack:
    def __init__(self):
        self.stack = []
        self.history = []
        self.len_s = 0
        self.len_h = 0

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.len_s += 1
        if len(self.stack) == 1:
            self.history.append(val)
        else:
            self.history.append(min(val, self.history[-1]))
        self.len_h += 1
        


    def pop(self) -> None:
        self.stack.pop()
        self.history.pop()

        self.len_s -= 1
        self.len_h -= 1


    def top(self) -> int:
        return self.stack[self.len_s-1]
        
        
    def getMin(self) -> int:
        return self.history[self.len_h-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()