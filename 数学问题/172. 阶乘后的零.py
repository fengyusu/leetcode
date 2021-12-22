class Solution:
    def trailingZeroes1(self, n: int) -> int:
        res = 0
        while n > 0:
            n //= 5
            res += n
        return res

    def trailingZeroes(self, n: int) -> int:
        return 0 if n<5 else n//5 + self.trailingZeroes(n//5)

