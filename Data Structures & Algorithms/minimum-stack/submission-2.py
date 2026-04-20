class MinStack:

    def __init__(self):
        # create two stacks the main stack and the getMinStack
        self.stack = []
        self.miniStack = []

    def push(self, val: int) -> None:
        # push or append the val to both stacks
        self.stack.append(val)
        val = min(val, self.miniStack[-1] if  self.miniStack else val)
        self.miniStack.append(val)        

    def pop(self) -> None:
        # pop val from both stacks
        self.stack.pop()
        self.miniStack.pop()

    def top(self) -> int:
        # return the top element from main stack
        return self.stack[-1]

    def getMin(self) -> int:
        # return the current minimum value in the miniStack. 
        return self.miniStack[-1]
