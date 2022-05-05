
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 ] *n for i in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = 1
                elif i == 0:
                    dp[i][j] = dp[i][ j -1]
                elif j == 0:
                    dp[i][j] = dp[ i -1][j]
                else:
                    dp[i][j] = dp[i][ j -1] + dp[i - 1][j]
        return dp[ m -1][ n -1]