from typing import List
import sys

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        if n == 0:
            return -1
        dp = [sys.maxsize]*(amount+1)
        res = dp[amount]
        dp[0] = 0
        for i in range(1, n+1):
            coin = coins[i-1]
            for j in range(coin, amount+1):
                dp[j] = min(dp[j], dp[j-coin]+1)
        if res == dp[amount]:
            return -1
        return dp[amount]



if __name__ == '__main__':
    arr = [1]


    solution = Solution()
    res = solution.coinChange(arr,0)
    print("res", res)