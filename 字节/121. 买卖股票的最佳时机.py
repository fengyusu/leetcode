import sys
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        buy = -prices[0]
        sell = 0
        for i in range(1, len(prices)):
            sell = max(sell, buy + prices[i])
            buy = max(buy, -prices[i])
        return sell
