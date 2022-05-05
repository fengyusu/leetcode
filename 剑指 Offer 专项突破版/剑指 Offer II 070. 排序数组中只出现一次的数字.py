from typing import List

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res = res ^ num
        return res

    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == nums[mid^1]:
                left = mid + 1
            else:
                right = mid
        return nums[left]

