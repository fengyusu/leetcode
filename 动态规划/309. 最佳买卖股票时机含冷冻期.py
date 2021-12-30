from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n <= 1:
            return 0
        buy = -prices[0]
        sell = 0
        rest = 0
        for i in range(1,n):
            buy_tmp = max(buy, rest - prices[i])
            sell_tmp = buy_tmp + prices[i]
            rest_tmp = max(rest, sell)
            buy = buy_tmp
            sell = sell_tmp
            rest = rest_tmp
        return max(sell, rest)