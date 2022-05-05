import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        if n == h:
            return max(piles)

        def cost(piles, k):
            return sum([math.ceil(p / k) for p in piles])

        res = max(piles)
        left = 1
        right = max(piles)
        while left <= right:
            mid = left + (right - left) // 2
            if cost(piles, mid) <= h:
                res = mid
                right = mid - 1
            else:
                left = mid + 1

        return res



