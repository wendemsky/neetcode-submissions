class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False
        stack = []
        i = 0
        print(stack)
        while i <= len(s)-1:
            if (s[i] == '(' or s[i] == '[' or s[i] == '{'):
                stack.append(s[i])
            elif stack and ((stack[-1] == '(' and s[i] == ')')
                or (stack[-1] == '{' and s[i] == '}')
                or (stack[-1] == '[' and s[i] == ']')):
                stack.pop()
            else:
                return False
            i += 1

        return len(stack) == 0