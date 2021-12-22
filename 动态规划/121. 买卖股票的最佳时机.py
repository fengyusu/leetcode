from typing import List
import sys

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = -sys.maxsize
        sell = 0
        for price in prices:
            buy = max(buy, -price)
            sell = max(sell, buy + price)
        return sell