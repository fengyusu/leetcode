from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        nums.sort()
        i = 0
        while i < n - 2 and nums[i] <= 0:
            target = -nums[i]
            l = i + 1
            r = n - 1
            while l < r:
                cur_val = nums[l] + nums[r]
                if cur_val == target:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    r -= 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif cur_val > target:
                    r -= 1
                elif cur_val < target:
                    l += 1
            i += 1
            while i < n and nums[i] == nums[i - 1]:
                i += 1

        return res