from typing import List


class Solution:
    def helper(self, nums, start, end):
        first = nums[start]
        second = max(first, nums[start+1])
        for i in range(start+2, end+1):
            first, second = second, max(first+nums[i], second)
        return second
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0],nums[1])
        return max(self.helper(nums, 0, n-2), self.helper(nums, 1, n-1))
