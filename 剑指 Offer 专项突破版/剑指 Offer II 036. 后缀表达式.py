from typing import List
import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        values = []
        for t in tokens:
            # print("t ", t)
            if t.isdigit() or t.strip('-').isdigit():
                values.append(int(t))
            elif t == '+':
                a = values.pop()
                b = values.pop()
                values.append(a+b)
            elif t == '-':
                a = values.pop()
                b = values.pop()
                values.append(b-a)
            elif t == '*':
                a = values.pop()
                b = values.pop()
                values.append(a*b)
            elif t == '/':
                a = values.pop()
                b = values.pop()

                values.append(int(b / a))
            # print("values ", values)
        return values[0]

sln = Solution()
res = sln.evalRPN(tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
