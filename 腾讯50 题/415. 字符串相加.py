
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        l1 = len(num1)
        l2 = len(num2)
        if l1 < l2:
            return self.addStrings(num2, num1)
        res = []
        overflow = 0
        for i in range(l1):
            cur_val = 0
            if i < l2:
                c1 = ord(num1[l1-i-1]) - ord('0')
                c2 = ord(num2[l2-i-1]) - ord('0')
                cur_val = (c1+c2+overflow)
            else:
                c1 = ord(num1[l1 - i - 1]) - ord('0')
                cur_val = (c1 + overflow)
            res.append(cur_val % 10)
            overflow = cur_val // 10
        if overflow:
            res.append(1)
        n = len(res)
        return ''.join([str(res[n-i-1]) for i in range(n)])