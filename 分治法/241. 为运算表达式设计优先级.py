

class Solution:
    def diffWaysToCompute(self, expression: str):
        ways = []
        n = len(expression)
        for i in range(n):
            c = expression[i]
            if c == '+' or c == '*' or c == '-':
                left = self.diffWaysToCompute(expression[0:i])
                right = self.diffWaysToCompute(expression[i+1:])
                for l in left:
                    for r in right:
                        if c == '+':
                            ways.append(l+r)
                        elif c == '-':
                            ways.append(l-r)
                        else:
                            ways.append((l*r))
        if len(ways) == 0:
            return [int(expression)]
        return ways

if __name__ == '__main__':
    arr = "21"
    solution = Solution()
    result = solution.diffWaysToCompute(arr)
    print(result)