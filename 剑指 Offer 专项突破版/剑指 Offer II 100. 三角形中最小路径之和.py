from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        h = len(triangle)
        if h == 0:
            return 0

        dp = [[0] * (i+1) for i in range(h)]
        dp[0][0] = triangle[0][0]
        for i in range(1,h):
            for j in range(i+1):
                if j == 0:
                    dp[i][j] = dp[i-1][j] + triangle[i][j]
                elif j == i:
                    dp[i][j] = dp[i - 1][j-1] + triangle[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j-1]) + triangle[i][j]
        return min(dp[h-1])
