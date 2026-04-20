class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # intuition - create a stack
        stack = []

        # for each character in the string tokens, create conditions for the operators
        for c in tokens:
            if c == '+':
                stack.append(stack.pop() + stack.pop())
            elif c == '-':
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == '*':
                stack.append(stack.pop() * stack.pop())
            elif c == '/':
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b)/a))
            # If not an operator, it's a number and change from char to int
            else:
                stack.append(int(c))
            
        return stack[0]
            