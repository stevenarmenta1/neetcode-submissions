class MinStack:

    def __init__(self):
        # Create the main stack and an accessory 2nd Get min stack. 
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        # Push/ append the val to the main stack and update the min if applicable and then store in minstack
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val) # if there is a value in minStack else it would be val
        self.minStack.append(val) # Append the min value to be stored in the 2nd stack

    def pop(self) -> None:
        # pop from both stacks
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        # Return the top element from the main stack. 
        return self.stack[-1]

    def getMin(self) -> int:
        # return the top element or the minimum value stored in the 2nd Min stack
        return self.minStack[-1]
