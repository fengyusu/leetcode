

class Solution:
    def dfs(self, heights, can_reach, r, c):
        dir = [-1, 0, 1, 0, -1]
        if can_reach[r][c]:
            return
        m = len(heights)
        n = len(heights[0])
        can_reach[r][c] = True
        for i in range(4):
            x = r + dir[i]
            y = c + dir[i + 1]
            if x >= 0 and x <= m and y >= 0 and y < n and heights[x][y] >= heights[r][c]:
                self.dfs(heights, can_reach, x, y)

    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        if len(heights) == 0 or len(heights[0]) == 0:
            return []
        res = []
        m = len(heights)
        n = len(heights[0])
        can_reach_p = [[False]*n for i in range(m)]
        can_reach_a = [[False] * n for i in range(m)]
        for i in range(n):
            self.dfs(heights, can_reach_p, 0, i)
            self.dfs(heights, can_reach_a, m-1, i)
        for j in range(m):
            self.dfs(heights, can_reach_p, j, 0)
            self.dfs(heights, can_reach_a, j, n-1)
        for i in range(m):
            for j in range(n):
                if can_reach_p[i][j] and can_reach_a[i][j]:
                    res.append([i,j])
        return res

