

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)
        if m == 0:
            return 0
        if n == 0:
            return 1

        dp = [[1]*(m+1) if i == 0 else [0]*(m+1) for i in range(n+1)]

        for i in range(1, n+1):
            for j in range(1, m+1):
                if s[j-1] == t[i-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
                else:
                    dp[i][j] = dp[i][j - 1]

        return dp[n][m]


sln = Solution()
print(sln.numDistinct(s = "rabbbit", t = "rabbit"))

