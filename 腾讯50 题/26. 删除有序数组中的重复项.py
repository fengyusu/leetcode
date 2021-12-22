from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return n
        new_index = 1
        prev_val = nums[0]
        for i in range(1, n):
            if nums[i] == prev_val:
                continue
            prev_val = nums[i]
            nums[new_index] = nums[i]
            new_index += 1
        return new_index