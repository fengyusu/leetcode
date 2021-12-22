from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        dict = {}
        for i in range(n):
            if nums[i] in dict.keys():
                dict[nums[i]] += 1
            else:
                dict[nums[i]] = 1
        max_key = nums[0]
        for k in dict.keys():
            if dict[k] > dict[max_key]:
                max_key = k
        return max_key
