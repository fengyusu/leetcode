from collections import deque

class Solution:
    def shortestBridge(self, grid) -> int:
        m = len(grid)
        n = len(grid[0])
        stack = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    stack.append((i, j))
                    break
            else:
                continue
            break

        first_level = []
        dir = [-1,0,1,0,-1]
        while len(stack):
            (x, y) = stack.pop()
            grid[x][y] = 2
            for i in range(4):
                r = x + dir[i]
                c = y + dir[i+1]
                if r >= 0 and r < m and c >= 0 and c < n:
                    if grid[r][c] == 1:
                        stack.append((r, c))
                    elif grid[r][c] == 0:
                        first_level.append((r,c))


        my_deque = deque(first_level)
        print(my_deque)
        level = 0
        while len(my_deque):
            level += 1
            cur_level_points = len(my_deque)
            while cur_level_points:
                cur_level_points -= 1
                (x,y) = my_deque.popleft()
                for i in range(4):
                    r = x + dir[i]
                    c = y + dir[i + 1]
                    if r >= 0 and r < m and c >= 0 and c < n:
                        if grid[r][c] == 1:
                            return level
                        if grid[r][c] == 2:
                            continue
                        my_deque.append((r,c))
                        grid[r][c] = 2
        return 0





if __name__ == '__main__':
    arr = [[0,1,0],[0,0,0],[0,0,1]]
    solution = Solution()
    res = solution.shortestBridge(arr)
    print(res)

