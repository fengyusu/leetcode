from typing import List

class Solution:

    def back_tracking(self, nums, level, cur, res):
        if level == len(nums):
            res.append(cur.copy())
            return


        cur.append(nums[level])
        self.back_tracking(nums, level + 1, cur, res)
        cur.pop()
        self.back_tracking(nums, level + 1, cur, res)



    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        cur = []
        self.back_tracking(nums, 0, cur, res)
        return res
