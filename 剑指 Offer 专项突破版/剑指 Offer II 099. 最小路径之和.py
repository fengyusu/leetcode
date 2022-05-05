from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        dp = [[0 ] *n for i in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = grid[0][0]
                elif i == 0:
                    dp[i][j] = dp[i][ j -1] + grid[i][j]
                elif j == 0:
                    dp[i][j] = dp[ i -1][j] + grid[i][j]
                else:
                    dp[i][j] = min(dp[i][ j -1], dp[i - 1][j]) + grid[i][j]
        return dp[ m -1][ n -1]