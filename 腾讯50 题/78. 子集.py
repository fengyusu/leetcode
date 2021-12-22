from typing import List


class Solution:
    def subsets0(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n == 1:
            return [[],nums]

        cur_val = nums[n-1]
        next_sets = self.subsets(nums[:n-1])
        print("curval",cur_val)
        print("next_set",next_sets)
        res = next_sets.copy()
        for i in range(len(next_sets)):
            new_set = next_sets[i].append(cur_val)
            res.append(new_set)
        print("after", res)
        return res

    def backTracking(self, nums, level):
        if level == len(nums):
            self.res.append(self.cur_set.copy())
            return

        self.cur_set.append(nums[level])
        self.backTracking(nums, level+1)
        self.cur_set.pop()
        self.backTracking(nums, level+1)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        self.cur_set = []
        self.res = []
        self.backTracking(nums, 0)
        return self.res

if __name__ == '__main__':
    s = [1,2,3]
    solution = Solution()
    result = solution.subsets(s)
    print(result)
