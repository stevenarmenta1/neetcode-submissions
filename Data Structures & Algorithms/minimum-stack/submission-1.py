class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        # remove the top element from both stacks. 
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        # return the top element of the main stack
        return self.stack[-1]

    def getMin(self) -> int:
        # return the top element of the accessory minStack.
        return self.minStack[-1]
