from typing import List

class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        cur_index = 0
        for i in range(len(nums)):
            if nums[i] % 2:
                nums[i], nums[cur_index] = nums[cur_index],nums[i]
                cur_index += 1
        return nums
