from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        dp = [0]*(n+1)
        for i in range(1,n+1):
            x = nums[i-1]
            dp[i] = max(dp[i-1]+x, x)
        print(dp)
        return max(dp[1:])

if __name__ == '__main__':
    s = [-2,-1]

    solution = Solution()
    result = solution.maxSubArray(s)
    print(result)

