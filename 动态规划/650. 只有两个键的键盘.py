import math

class Solution:
    def minSteps(self, n: int) -> int:
        if n < 2:
            return 0
        dp = [0]*(n+1)
        h = int(math.sqrt(n))
        for i in range(2, n+1):
            dp[i] = i
            for j in range(2, h+1):
                if i % j == 0:
                    dp[i] = dp[j] + dp[i//j]
                    break
            print("{}:{}".format(i,dp[i]))
        return dp[n]

if __name__ == '__main__':

    solution = Solution()
    res = solution.minSteps(10)
    print("res", res)