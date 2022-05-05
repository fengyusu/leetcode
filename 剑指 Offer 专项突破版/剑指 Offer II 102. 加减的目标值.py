from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        max_edge = sum(nums)

        dp = {i:0 for i in range(-max_edge, max_edge+1)}
        dp[0] = 1
        if target not in dp:
            return 0

        for num in nums:
            new_dp = {}
            for i in range(-max_edge, max_edge+1):
                cur_target = 0
                cur_target += dp[i + num] if i+num in dp else 0
                cur_target += dp[i - num] if i - num in dp else 0
                new_dp[i] = cur_target
            dp = new_dp
        # print(dp)

        return dp[target]

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        self.res = 0

        def dfs(cur_index, cur_sum):
            if cur_index == n :
                if cur_sum == target:
                    self.res += 1
                return

            dfs(cur_index + 1, cur_sum + nums[cur_index])
            dfs(cur_index + 1, cur_sum - nums[cur_index])

        dfs(0,0)
        return self.res


sln = Solution()
print(sln.findTargetSumWays(nums = [1,1,1,1,1], target = 3))