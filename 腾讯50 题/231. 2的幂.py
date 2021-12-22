
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        if n == 1:
            return True
        if n % 2:
            return False
        while n / 2 != 1:
            n /= 2
            if n % 2:
                return False
        return True

    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n&(n-1)) == 0

if __name__ == '__main__':
    s = 0
    solution = Solution()
    result = solution.isPowerOfTwo(s)
    print(result)