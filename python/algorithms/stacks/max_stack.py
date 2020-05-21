class MaxStack:

    def __init__(self):
        self.stack = []
        self.maxStack = []
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.maxStack:
            self.maxStack.append(x)
        else:
            curMax = max(x, self.maxStack[-1])
            self.maxStack.append(curMax)

    def pop(self) -> int:
        elem = self.stack.pop()
        self.maxStack.pop()
        return elem

    
    def top(self) -> int:
        return self.stack[-1]
        

    def peekMax(self) -> int:
        return self.maxStack[-1]
        

    def popMax(self) -> int:
        tmpStack = []
        elem = self.maxStack[-1]
        while self.stack[-1] != elem:
            tmpStack.append(self.stack.pop())
            self.maxStack.pop()
            
        self.stack.pop()
        self.maxStack.pop()
        while tmpStack:
            elem1 = tmpStack.pop()
            if self.maxStack:
                curMax = max(elem1, self.maxStack[-1])
            else:
                curMax = elem1
            self.stack.append(elem1)
            self.maxStack.append(curMax)
        return elem