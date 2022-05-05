from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        if m == 1 and n == 1 :
            return 1

        max_cache = [[-1]*n for i in range(m)]
        dir = [-1, 0, 1, 0, -1]
        def dfs(i,j):
            res = 1
            for k in range(4):
                x = i+dir[k]
                y = j+dir[k+1]
                if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
                    if max_cache[x][y] == -1:
                        max_cache[x][y] = dfs(x, y)
                    res = max(res, max_cache[x][y]+1)
            return res

        res = 1
        for i in range(m):
            for j in range(n):
                res = max(res, dfs(i,j))
        return res
