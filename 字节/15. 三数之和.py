from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        n = len(nums)
        i = 0
        while i < n:
            if nums[i] > 0:
                break
            target = -nums[i]
            l = i + 1
            r = n - 1
            while l < r:
                local_target = nums[l] + nums[r]
                if local_target == target:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l = l + 1
                    while l < r and nums[r] == nums[r-1]:
                        r = r - 1
                    r -= 1
                    l += 1
                elif local_target > target:
                    r -= 1
                else:
                    l += 1
            i += 1
            while i > 0 and i < n and nums[i] == nums[i-1]:
                i += 1
        return res