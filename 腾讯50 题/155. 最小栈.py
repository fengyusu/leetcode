import sys

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minstack = [sys.maxsize]


    def push(self, val: int) -> None:
        self.stack.append(val)
        self.minstack.append(min(val, self.minstack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()

    def top(self) -> int:
        if len(self.stack):
            return self.stack[-1]
        else:
            return None


    def getMin(self) -> int:
        return self.minstack[-1]

