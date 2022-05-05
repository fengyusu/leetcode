from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        nums.sort()

        n = len(nums)
        res = []
        vis = [False]*n
        def backtracking(cur_cand, level):
            if level == n:
                res.append(nums.copy())

            for i in range(n):
                if vis[i] or (i > 0 and nums[i] == nums[i-1] and not vis[i-1]):
                    continue
                cur_cand.append(nums[i])
                vis[i] = True
                backtracking(cur_cand, level + 1)
                cur_cand.pop()
                vis[i] = False

        cur_cand = []
        backtracking(cur_cand, 0)
        return res