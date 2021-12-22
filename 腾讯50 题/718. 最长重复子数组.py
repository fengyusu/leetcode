from typing import List


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m = len(nums1)
        n = len(nums2)
        dp = [[0]*(n+1) for i in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                num1 = nums1[i-1]
                num2 = nums2[j-1]
                if num1 != num2:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j-1] + 1
        res = 0
        for i in range(m+1):
            res = max(res, max(dp[i]))
        return res