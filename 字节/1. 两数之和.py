from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        if n < 2:
            return []
        previous_nums = nums.copy()
        nums.sort()
        l = 0
        r = n - 1
        while l < r:
            local_target = nums[l] + nums[r]
            if local_target == target:
                if nums[l] != nums[r]:
                    return [previous_nums.index(nums[l]), previous_nums.index(nums[r])]
                else:
                    return []
            elif local_target > target:
                while r > 0 and nums[r-1] == nums[r]:
                    r -= 1
                r -= 1
            else:
                while l < n-1 and nums[l+1] == nums[l]:
                    l += 1
                l += 1
        return []


