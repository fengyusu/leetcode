from typing import List

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l = 0
        r = 0
        res = 0
        total = 1
        while r < n:
            total *= nums[r]
            while l <= r and total >= k:
                total /= nums[l]
                l += 1
            res += r - l + 1
            r += 1
        return res