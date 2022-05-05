from typing import List

class Solution:
    def dfs(self, grid, visited, i, j):
        if visited[i][j]:
            return 0
        visited[i][j] = True
        if grid[i][j] == 0:
            return 0
        else:
            cur_area = 1
            dir = [-1,0,1,0,-1]
            for k in range(4):
                x = i + dir[k]
                y = j + dir[k+1]
                if x >=0 and x < self.m and y >= 0 and y < self.n:
                    cur_area += self.dfs(grid, visited, x, y)
            return cur_area


    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.m = len(grid)
        self.n = len(grid[0])

        res = 0

        visited = [[False]*self.n for i in range(self.m)]

        for i in range(self.m):
            for j in range(self.n):
                cur_area = self.dfs(grid, visited, i, j)
                res = max(res, cur_area)
                # print(cur_area)

        return res

sln = Solution()
print(sln.maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]))