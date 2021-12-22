from typing import List
import sys

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closest = sys.maxsize
        nums.sort()
        n = len(nums)
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            cur_target = target - nums[i]
            l = i+1
            r = n-1
            while l < r:
                cur_val = nums[l] + nums[r]
                if abs(cur_val - cur_target) < abs(closest - target):
                    closest = cur_val + nums[i]
                if cur_val == cur_target:
                    return target
                elif cur_val > cur_target:
                    r -= 1
                else:
                    l += 1
        return closest
