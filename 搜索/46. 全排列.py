

class Solution:
    def swap(self, num, i, j):
        num[i],num[j] = num[j],num[i]

    def backTracking(self, nums, level, res):
        if level == len(nums)-1:
            res.append(nums.copy())
            return
        for i in range(level, len(nums)):
            self.swap(nums, level, i)
            self.backTracking(nums, level+1, res)
            self.swap(nums, level, i)


    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []
        self.backTracking(nums, 0, res)
        return res
