from typing import List


class Solution:
    def backTracking(self, nums, level, target):
        if level == len(nums):
            if self.cur_sum == target:
                self.count += 1
            return

        self.cur_sum += nums[level]
        self.backTracking(nums, level+1, target)
        self.cur_sum -= 2*nums[level]
        self.backTracking(nums, level+1, target)
        self.cur_sum += nums[level]

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.count = 0
        self.cur_sum = 0
        self.backTracking(nums, 0, target)
        return self.count

if __name__ == '__main__':
    arr = [1]
    solution = Solution()
    result = solution.findTargetSumWays(arr,1)
    print(result)