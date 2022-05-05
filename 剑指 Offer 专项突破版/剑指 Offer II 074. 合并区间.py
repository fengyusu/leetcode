from typing import List

class Solution:
    def upper_bound(self, nums, val):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if val == nums[mid][1]:
                right = mid - 1
            elif val < nums[mid][1]:
                right = mid - 1
            elif val > nums[mid][1]:
                left = mid + 1
        return left

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        if n == 0:
            return []

        intervals.sort(key=lambda x : [x[1],x[0]])
        res = [intervals[0]]
        for i in range(1, n):
            cur_interval = intervals[i]
            upper_index = self.upper_bound(res, cur_interval[0])
            if upper_index == len(res):
                res.append(cur_interval)
            else:
                new_interval = [min(cur_interval[0], res[upper_index][0]), cur_interval[1]]
                res = res[:upper_index] + [new_interval]
        return res



