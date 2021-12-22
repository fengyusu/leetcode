import sys
import math

class Solution:
    def numSquares(self, n: int) -> int:
        dp = [sys.maxsize] * (n+1)
        dp[0] = 0
        for i in range(1,n+1):
            j = 1
            j_end = int(math.sqrt(i))
            while j <= j_end:
                dp[i] = min(dp[i], dp[i-j**2]+1)
                j += 1
            # print(dp)
        return dp[n]

if __name__ == '__main__':
    arr = []

    solution = Solution()
    res = solution.numSquares(2278)
    print("res", res)