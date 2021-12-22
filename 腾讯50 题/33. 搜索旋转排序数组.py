from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 0:
            return -1
        if n == 1:
            if target == nums[0]:
                return 0
            else:
                return -1
        l = 0
        r = n-1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            else:
                if nums[mid] < nums[r]:
                    if nums[mid] < target and nums[r] >= target:
                        l = mid + 1
                    else:
                        r = mid - 1
                else:
                    if nums[mid] > target and nums[l] <= target:
                        r = mid - 1
                    else:
                        l = mid + 1
        if l > r:
            return -1