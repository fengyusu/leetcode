from typing import List

##0-1 背包问题
def knapsack01(weights:List[int], values:List[int], n, w):
    dp = [[0]*(w+1) for i in range(n+1)]
    for i in range(1, n+1):
        weight = weights[i-1]
        value = values[i-1]
        for j in range(1, w+1):
            if j >= weight:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight]+value)
            else:
                dp[i][j] = dp[i-1][j]
        return dp[n][w]

##完全背包问题
def knapsack0n(weights:List[int], values:List[int], n, w):
    dp = [[0]*(w+1) for i in range(n+1)]
    for i in range(1, n+1):
        weight = weights[i-1]
        value = values[i-1]
        for j in range(1, w+1):
            if j >= weight:
                dp[i][j] = max(dp[i-1][j], dp[i][j-weight]+value)
            else:
                dp[i][j] = dp[i-1][j]
        return dp[n][w]