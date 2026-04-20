class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b-a) # append b - a.
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
            # else it is a number, make sure we return an int, not a character
                a, b = stack.pop(), stack.pop()
                stack.append(int(b/a))
            else:
                stack.append(int(c))
                
        return stack[0]