from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 3:
            return max(nums)

        def rob_range(start, end):
            first = nums[start]
            second = max(first, nums[start + 1])
            for i in range(start+2, end+1):
                first, second = second, max(nums[i]+first, second)
            return second

        return max(rob_range(1,n-1), rob_range(0,n-2))