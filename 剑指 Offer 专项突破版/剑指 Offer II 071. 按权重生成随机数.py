import random
from typing import List
from itertools import accumulate
import bisect

class Solution:

    def __init__(self, w: List[int]):
        w_sum = sum(w)
        self.w = list(accumulate([i/w_sum for i in w]))

    def upper_bound(self, nums, val):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if val == nums[mid]:
                right = mid - 1
            elif val < nums[mid]:
                right = mid - 1
            elif val > nums[mid]:
                left = mid + 1
        return left if left < len(nums) else len(nums) - 1

    def pickIndex(self) -> int:
        random_w = random.random()
        res = bisect.bisect_left(self.w, random_w)
        return res



# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()

print(bisect.bisect_right([1,1,2,3,4,4,4,5],1))
