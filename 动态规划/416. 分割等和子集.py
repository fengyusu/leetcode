from typing import List


class Solution:
    def canPartition0(self, nums: List[int]) -> bool:
        sums = sum(nums)
        if sums % 2:
            return False
        nums.sort(reverse=True)
        print(nums)
        n = len(nums)
        target = sums // 2
        dp = [[False]*(target+1) for i in range(n+1)]
        for i in range(n+1):
            dp[i][0] = True
        for i in range(1, n+1):
            num = nums[i-1]
            for j in range(num, target+1):
                dp[i][j] = dp[i-1][j] or dp[i-1][j-num]
        return dp[n][target]

    def canPartition(self, nums: List[int]) -> bool:
        sums = sum(nums)
        if sums % 2:
            return False
        nums.sort(reverse=True)
        print(nums)
        n = len(nums)
        target = sums // 2
        dp = [False for i in range(target+1)]
        dp[0] = True

        for i in range(1, n+1):
            num = nums[i-1]
            for j in range(target, num-1, -1):
                dp[j] = dp[j] or dp[j-num]
            print(num, dp)

        return dp[target]

if __name__ == '__main__':
    arr = [1,2,5,2]


    solution = Solution()
    res = solution.canPartition(arr)
    print("res", res)