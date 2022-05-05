from typing import List


class Solution:

    def back_tracking(self, rest, cur_cand):
        if self.n == len(cur_cand):
            self.res.append(cur_cand.copy())
            return

        for i in range(len(rest)):
            r = rest.pop(i)
            cur_cand.append(r)
            self.back_tracking(rest, cur_cand)
            rest.insert(i, r)
            cur_cand.pop()


    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        self.n = len(nums)
        self.res = []
        cur_cand = []
        self.back_tracking(nums, cur_cand)
        return self.res


    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        n = len(nums)
        res = []

        def backtracking(level):
            if level == n:
                res.append(nums.copy())

            for i in range(level, n):
                nums[level],nums[i] = nums[i],nums[level]
                backtracking(level + 1)
                nums[level], nums[i] = nums[i], nums[level]

        backtracking(0)
        return res