class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # 1 Intuition: Create a stack 
        stack = []

        # For every character in the string array tokens, 2 create each condition
        for c in tokens:
            if c == '+':
                stack.append(stack.pop() + stack.pop())
            elif c == '-':
                a, b = stack.pop(), stack.pop()
                stack.append(b-a)
            elif c == '*':
                stack.append(stack.pop() * stack.pop())
            elif c == '/':
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b)/a))
            else:
                stack.append(int(c)) # if not operator than it will be a number and convert to an int.  
        
        return stack[0]