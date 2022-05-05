import sys
from typing import List

class Solution:

    def minCut(self, s: str) -> int:
        n = len(s)

        f = [[True]*n for i in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                f[i][j] = (s[i] == s[j]) and f[i+1][j-1]

        dp = [n+1]*n

        for i in range(n):
            if f[0][i]:
                dp[i] = 0
            else:
                for j in range(i):
                    if f[j+1][i]:
                        dp[i] = min(dp[i], dp[j]+1)

        return dp[n-1]


sln = Solution()
print(sln.minCut("ab"))
