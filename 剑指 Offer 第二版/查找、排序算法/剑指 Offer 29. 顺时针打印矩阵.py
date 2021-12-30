from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        m = len(matrix)
        n = len(matrix[0])
        if n is 0:
            return []
        res = []
        prev_loc = [0, -1]
        dir = [[0,1], [1,0], [0,-1], [-1,0]]
        cur_dir_index = 0
        traveled = [[False]*n for _ in range(m)]
        for _ in range(m*n):
            x = prev_loc[0] + dir[cur_dir_index][0]
            y = prev_loc[1] + dir[cur_dir_index][1]
            if x < 0 or x >= m or y < 0 or y >= n or traveled[x][y]:
                cur_dir_index = (cur_dir_index + 1) % 4
                x = prev_loc[0] + dir[cur_dir_index][0]
                y = prev_loc[1] + dir[cur_dir_index][1]
            res.append(matrix[x][y])
            prev_loc = [x,y]
            traveled[x][y] = True
        return res



