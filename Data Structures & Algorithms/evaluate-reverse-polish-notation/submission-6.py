class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['+', '-', '*', '/']
        res = 0
        for c in tokens:
            if c in operators:
                b = stack[-1]
                stack.pop()
                a = stack[-1]
                stack.pop()
                res = 0
                if c == '+':
                    res = a + b
                elif c == '-':
                    res = a - b
                elif c == '*':
                    res = a * b
                else:
                    res = int(a / b)

                stack.append(res)
            else:
                stack.append(int(c))
        return stack[-1]