from typing import List



class Solution:
    def __init__(self):
        self.level = 0
        self.counts = 0

    def backTracking(self, n):
        print("level", self.level)
        if self.level > n:
            return
        if self.level == n:
            self.counts += 1
            print("counts ", self.counts)
            return

        self.level += 1
        self.backTracking(n)
        self.level -= 1

        self.level += 2
        self.backTracking(n)
        self.level -= 2

    def climbStairs0(self, n: int) -> int:
        self.backTracking(n)
        return self.counts

    def climbStairs1(self, n: int) -> int:
        dp = [1] * (n+1)
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

    def climbStairs(self, n: int) -> int:
        if n < 2:
            return n
        pre1 = 1
        pre2 = 1
        cur = 0
        for i in range(2, n+1):
            cur = pre1 + pre2
            pre2 = pre1
            pre1 = cur
        return cur


if __name__ == '__main__':
    arr = [[0,1,0],[0,0,0],[0,0,1]]
    solution = Solution()
    res = solution.climbStairs(35)
    print("res", res)