import sys
from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if n <= 1 or k <= 0:
            return 0
        if k >= n:
            res = 0
            for i in range(1, n):
                if prices[i] > prices[i - 1]:
                    res += prices[i] - prices[i - 1]
            return res

        buys = [-sys.maxsize] * k
        sells = [0] * k
        for price in prices:
            for i in range(k - 1, 0, -1):
                sells[i] = max(sells[i], buys[i] + price)
                buys[i] = max(buys[i], sells[i - 1] - price)
            sells[0] = max(sells[0], buys[0] + price)
            buys[0] = max(buys[0], -price)

        return sells[k - 1]