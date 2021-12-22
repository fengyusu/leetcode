
class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        stack = []
        for i in range(n):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                stack.append(s[i])
            elif s[i] == ')':
                if len(stack) != 0 and stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            elif s[i] == '}':
                if len(stack) != 0 and stack[-1] == '{':
                    stack.pop()
                else:
                    return False
            elif s[i] == ']':
                if len(stack) != 0 and stack[-1] == '[':
                    stack.pop()
                else:
                    return False
            else:
                return False
        if len(stack) != 0:
            return False
        else:
            return True