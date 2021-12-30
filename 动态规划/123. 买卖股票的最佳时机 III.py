import sys
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n <= 1:
            return 0

        buy1 = -sys.maxsize
        sell1 = 0
        buy2 = -sys.maxsize
        sell2 = 0

        for price in prices:
            sell2 = max(sell2, buy2 + price)
            buy2 = max(buy2, sell1 - price)
            sell1 = max(sell1, buy1 + price)
            buy1 = max(buy1, -price)

        return sell2