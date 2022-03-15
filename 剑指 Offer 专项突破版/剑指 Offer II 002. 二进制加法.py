

class Solution:
    def addBinary(self, a: str, b: str) -> str:

        if len(a) == 0 or len(b) == 0:
            return ""

        res = []
        carry = 0

        if len(a) < len(b):
            a,b=b,a

        a = list(a)
        b = ['0'] * (len(a) - len(b)) + list(b)

        for i in range(len(a)-1, -1, -1):
            c = int(a[i]) + int(b[i]) + carry
            if c <= 1:
                carry = 0
                res = [str(c)] + res
            else:
                carry = 1
                res = [str(1 if c == 3 else 0)] + res

        if carry == 0:
            return ''.join(res)
        else:
            return '1' + ''.join(res)





