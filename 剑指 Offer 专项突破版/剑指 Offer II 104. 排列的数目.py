from typing import List

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        if min(nums) > target:
            return 0

        n = len(nums)

        dp = [0]*(target+1)
        dp[0] = 1

        for num in nums:
            for i in range(num, target+1):
                dp[i] = dp[i-num] + dp[i]

        return dp[target]

    def combinationSum4(self, nums: List[int], target: int) -> int:
            dp = [1] + [0] * target
            for i in range(1, target + 1):
                for num in nums:
                    if num <= i:
                        dp[i] += dp[i - num]

            return dp[target]




    def combinationSum4(self, nums: List[int], target: int) -> int:
        min_num = min(nums)
        if min_num > target:
            return 0

        n = len(nums)
        self.count = 0

        def dfs(cur_sum):

            if cur_sum == target:
                self.count += 1
                return
            if cur_sum + min_num > target:
                return

            for num in nums:
                dfs(cur_sum + num)

        dfs(0)
        return self.count
