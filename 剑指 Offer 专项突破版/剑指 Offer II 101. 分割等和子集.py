from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        nums_sum = sum(nums)
        if nums_sum % 2 == 1:
            return False
        target = nums_sum // 2

        dp = [False] * (target+1)
        dp[0] = True

        for i in range(1, n+1):
            cur_num = nums[i-1]
            for j in range(target, cur_num-1 , -1):
                dp[j] = dp[j-cur_num] or dp[j]
                if j == target and dp[j]:
                    return True

        return dp[target]


