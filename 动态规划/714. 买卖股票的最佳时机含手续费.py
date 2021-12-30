import sys
from typing import List

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        if n <= 1:
            return 0
        buy = -sys.maxsize
        sell = 0
        for i in range(n):
            buy_tmp = max(buy, sell - prices[i] - fee)
            sell_tmp = max(sell, buy + prices[i])
            buy = buy_tmp
            sell = sell_tmp
        return sell

if __name__ == '__main__':
    arr = [1,2,3,4,6,7,8]
    solution = Solution()
    res = solution.maxProfit([1, 3, 2, 8, 4, 9], 2)
    print("res", res)