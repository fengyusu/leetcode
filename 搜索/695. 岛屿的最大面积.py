

class Solution:
    def maxAreaOfIsland0(self, grid: list[list[int]]) -> int:
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        m = len(grid)
        n = len(grid[0])
        area = 0
        dir = [0,1,0,-1,0]
        stack = []
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    grid[i][j] = 0
                    current_area = 0
                    stack.append((i,j))
                    while len(stack):
                        (r,c) = stack.pop()
                        current_area += 1
                        for k in range(4):
                            x = r + dir[k]
                            y = c + dir[k+1]
                            if x >= 0 and x < m and y >= 0 and y < n and grid[x][y]:
                                grid[x][y] = 0
                                stack.append((x,y))
                    area = max(area, current_area)
        return area

    def dfs(self, grid: list[list[int]], r, c):
        m = len(grid)
        n = len(grid[0])
        if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == 0:
            return 0
        grid[r][c] = 0
        return 1 + self.dfs(grid, r, c + 1) + self.dfs(grid, r, c - 1) + self.dfs(grid, r + 1, c) + self.dfs(grid, r - 1, c)

    def dfs(self, grid: list[list[int]], r, c):
        m = len(grid)
        n = len(grid[0])
        if grid[r][c] == 0:
            return 0
        grid[r][c] = 0
        area = 1
        dir = [-1,0,1,0,-1]
        for k in range(4):
            x = dir[k]
            y = dir[k+1]
            if x >= 0 and x < m and y >= 0 and y < n:
                area += self.dfs(grid, x, y)
        return area

    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:

        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        m = len(grid)
        n = len(grid[0])
        area = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    area = max(area, self.dfs(grid, i, j))
        return area

