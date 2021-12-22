from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n == 0:
            return [[]]
        if n == 1:
            return [[1]]
        res = [[0] * n for i in range(n)]
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dir_index = 0
        cur_pos = (0, -1)
        prev_pos = cur_pos
        for i in range(n * n):
            x = prev_pos[0] + dirs[dir_index][0]
            y = prev_pos[1] + dirs[dir_index][1]
            if x < 0 or x >= n or y < 0 or y >= n or res[x][y]:
                dir_index = (dir_index + 1) % 4
                x = prev_pos[0] + dirs[dir_index][0]
                y = prev_pos[1] + dirs[dir_index][1]
            print("pos", (x, y))
            res[x][y] = i+1
            prev_pos = (x, y)
        return res
        