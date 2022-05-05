

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        if x == 1:
            return 1
        left = 1
        right = x//2
        res = 1
        while left <= right:
            mid = left + (right - left) // 2
            if mid * mid <= x:
                res = mid
                left  = mid + 1
            else:
                right = mid - 1
        return res


