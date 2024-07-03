class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i == '+':
                stack.append(stack.pop() + stack.pop())
            elif i == '-':
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif i == '*':
                stack.append(stack.pop() * stack.pop())
            elif i == '/':
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            else:
                stack.append(int(i))
        return stack[0]


##### 2nd Approach ####
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        operators = ['+', '-', '*', '/']

        for i in range(len(tokens)):
            if tokens[i] in operators:
                m = stack.pop()
                n = stack.pop()
                x = int(eval(f"n {tokens[i]} m"))
                stack.append(int(x))
            else:
                stack.append(int(tokens[i]))
        
        return stack[-1] if stack else None

