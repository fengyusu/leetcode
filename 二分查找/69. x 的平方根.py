

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        s = 0
        e = x + 1
        while s < e - 1:
            m = (s + e) // 2
            m2 = m**2
            if m2 == x:
                return m
            elif m2 > x:
                e = m
            else:
                s = m
            print(s,e,m)
        return s


if __name__ == '__main__':
    solution = Solution()
    result = solution.mySqrt(10)
    print(result)