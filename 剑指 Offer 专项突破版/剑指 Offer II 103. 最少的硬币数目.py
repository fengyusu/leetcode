from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        n = len(coins)
        dp = [amount+1]*(amount+1)
        dp[0] = 0
        print(dp)
        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] = min(dp[i], dp[i-coin]+1)
            print(dp)

        return dp[-1] if dp[-1]!=(amount+1) else -1


sln = Solution()
print(sln.coinChange(coins = [1, 2, 5], amount = 11))