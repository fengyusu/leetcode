
class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return '0'
        is_neg = num < 0
        if is_neg:
            num = -num
        res = []
        while num:
            a = num // 7
            b = num % 7
            res = [str(b)] + res
            num = a
        if is_neg:
            res = ['-'] + res
        return ''.join(res)
