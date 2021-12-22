from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        counts = 0
        max_len = 0
        dict = {}
        dict[0] = -1
        for i in range(0, n):
            if nums[i]:
                counts += 1
            else:
                counts -= 1
            if counts in dict:
                max_len = max(max_len, i-dict[counts])
                dict[counts] = i
            else:
                dict[counts] = i
        return max_len

