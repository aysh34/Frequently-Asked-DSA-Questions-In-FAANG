class MyQueue:

    def __init__(self):
        self.inpStack = []
        self.outStack = []

    def push(self, x: int) -> None:
        self.inpStack.append(x)

    def pop(self) -> int:
        if self.outStack:
            return self.outStack.pop()
        else:
            while self.inpStack:
                self.outStack.append(self.inpStack.pop())
            return self.outStack.pop()

    def peek(self) -> int:
        if self.outStack:
            return self.outStack[-1]
        else:
            while self.inpStack:
                self.outStack.append(self.inpStack.pop())
            return self.outStack[-1]

    def empty(self) -> bool:
        if not self.inpStack and not self.outStack:
            return True
        return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()