

class Solution:
    def isDigit(self,c):
        return True if ord(c) >= ord('0') and ord(c) <= ord('9') else False

    def parseNum(self,s,i):
        n = 0
        while i < len(s) and self.isDigit(s[i]):
            n = n*10 + int(s[i])
            i += 1
        return n,i


    def parseExpr(self,s,i):
        op = '+'
        l = r = 0
        while i < len(s):
            if s[i] != " ":
                n,i = self.parseNum(s,i)
                if op == '+':
                    l += r
                    r = n
                elif op == '-':
                    l += r
                    r = -n
                elif op == '*':
                    r = r * n
                elif op == '/':
                    r = int(r / n)

                if i < len(s):
                    op = s[i]
            i += 1

        return l+r


    def calculate(self, s: str) -> int:
        i = 0
        return self.parseExpr(s, i)

if __name__ == '__main__':
    arr = "14-3/2"
    solution = Solution()
    result = solution.calculate(arr)
    print(result)