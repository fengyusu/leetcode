from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1]*n
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)

if __name__ == '__main__':
    arr = [0,1,0,3,2,3]
    solution = Solution()
    res = solution.lengthOfLIS(arr)
    print("res", res)

